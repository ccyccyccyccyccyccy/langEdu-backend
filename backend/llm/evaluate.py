import os
import csv
from dotenv import load_dotenv
from typing import Optional, List, Tuple
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, Field
from langchain.schema import BaseCache, LLMResult
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import json
from supabase import create_client, Client
import random
from tqdm import tqdm
from db import Qtype

from user import get_supabase, get_client_session

class EvaluationQ(BaseModel):
    """Information about a question."""
    QA : str = Field(
        description="The question-answer pair."
    )
    
    def __str__(self):
        #return f"Question: {self.question}, Answer: {self.answer}"
        return "Question: " + self.QA

class ExtractionData(BaseModel):
    """Extracted information about questions in documents."""
    questions: List[EvaluationQ]

# Function to extract questions from json file for evaluation
def extract_questions_eval(file_path: str):  # Input: file path to json file
    # Load the json file
    contents = []
    with open(file_path, 'r') as f:
        contents = json.load(f)["content"]
    # Define a custom prompt to provide instructions and any additional context
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert at extracting a question. "
                "Include the COMPLETE question text, including possible options for MCQs, if any.",
            ),
            ("human", "{text}"),
        ]
    )

    # Instantiate the AzureChatOpenAI model
    
    llm = AzureChatOpenAI(
        azure_deployment="gpt-4o-mini",  # Replace with your deployment
        api_version="2024-10-01-preview",  # Replace with your API version
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    

    # Rebuild the model to finalize it
    AzureChatOpenAI.model_rebuild()

    # Create an extractor with structured output
    extractor = prompt | llm.with_structured_output(
        schema=ExtractionData,
        include_raw=False,
    )

    # Process the first few texts

    extractions = extractor.batch(
        [{"text": t["questions"]} for t in contents], 
        {"max_concurrency": 5},  # Limit concurrency
    )

    # Collect extracted key concepts
    all_questions = []
    for extraction in extractions:
        all_questions.extend(extraction.questions)

    return all_questions

def test_extract_questions_eval():
    # Test the extraction function with a sample file path
    file_path = r"output\questions_v1.0_withPP.json"
    extracted_questions = extract_questions_eval(file_path)
    for question in extracted_questions:
        print(question)

class Evaluator():

    def __init__(self, model_name: str=None, api_key: str=None, api_version: str=None):
        if model_name is None:
            model_name= "gpt-4o"
        if api_key is None:
            api_key = os.getenv("AZURE_OPENAI_API_KEY")
        if api_version is None:
            api_version = "2024-10-01-preview"
        self.model_name = model_name
        self.api_key = api_key
        self.api_version = api_version
        self.session_id = get_client_session()
        print(f"Using supabase Client Session: {self.session_id}")
        self.supabase = get_supabase()

    def _judge(self, QA:str, subject_name:str, question_type:str, compareQA:list[str]) -> str:
        """
        Judge the quality of a question based on its content and compare it with other questions.
        Args:
            QA (str): The question-answer pair to be judged.
            subject (str): The subject of the question.
            question_type (str): The type of the question.
            compareQA (list[str]): List of question-answer pairs to compare against.
        Returns:

        """
        if not len(compareQA) == 2:
            raise ValueError("compareQA must contain exactly 2 question-answer pairs for comparison.")
        judge_prompt = ChatPromptTemplate.from_messages(
            [
                (   "system",
                    "You are a judge evaluating the quality of assessment questions. "
                    "You will be given 3 question-answer pairs."
                    "Determine which question is the odd one out based on the quality of the question, for example, the depth of the question, the relevance to the subject."
                    "Do not consider the exact topic, or the format of the question, but rather the quality of the question itself."
                    "You should answer 'Pair1', 'Pair2', 'Pair3' depending on which question is the odd one out. You may also answer 'None' if all questions are of similar quality. No other text is allowed in the response."
                ),
                ("human", "The subject is {subject_name}. Type: {question_type}. Pair1: {QA}\n Pair2: {pair2}\n Pair3: {pair3}"),
            ]
        )
        llm = AzureChatOpenAI(
            azure_deployment=self.model_name,
            api_version=self.api_version,
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            api_key=self.api_key
    )

        judge_chain = judge_prompt | llm | StrOutputParser()
        result = judge_chain.invoke({"subject_name": subject_name, "question_type": question_type, "QA": QA, "pair2": compareQA[0], "pair3": compareQA[1]})
        if "pair1" in result.lower():
            return True
        elif "pair2" in result.lower() or "pair3" in result.lower() or "none" in result.lower():
            return False
        else:
            raise ValueError("Unexpected response from judge chain: " + result)
        
    def _majority_vote(self, question: str, subject: str, question_type: str, compare_questions_all: list[str], k=5) -> bool:
        """
        Determine the majority vote among the comparison questions.
        Args:
            question (str): The original question.
            subject (str): The subject of the question.
            question_type (str): The type of the question.
            compare_questions (list[str]): List of question-answer pairs to compare against.
        Returns:
            bool: True if the majority agrees with the original question, False otherwise.
        """
        if len(compare_questions_all) < 2:
            raise ValueError("compare_questions must contain at least two questions.")

        votes = []
        for i in range(k): 
            compare_questions = random.sample(compare_questions_all, 2)
            result = self._judge(question, subject, question_type, compare_questions)
            votes.append(result)
        return sum(votes)/ len(votes)

    def benchmark(self, subject, question_type, k=5):
        """
        the subject should be the same as the subject in the database.
        question_type should be one of the Qtype enum values defined in db.py
        """
        mcqs = self.supabase.table("document").select("*").eq("session_id", self.session_id).eq("subject", subject).eq("question_type", question_type).execute()
        QAPairs=[]
        benchmark_results = []
        for mcq in mcqs.data:
            QA = "Question: " + mcq["data"]["Question"] + " Answer: " + mcq["data"]["Answer"]
            QAPairs.append(QA)
        for QA in QAPairs:
            compare_questions = QAPairs.copy()
            compare_questions.pop(compare_questions.index(QA))
            result = self._majority_vote(QA, subject, question_type, compare_questions, k=k)
            benchmark_results.append(result)
        print(f"Benchmark results for {subject}: {sum(benchmark_results) / len(benchmark_results)}")
    
    def evaluate(self, file_path: str, subject: str, question_type: str,k=5, save_results:bool= False) -> float:
        if question_type not in Qtype.__members__:
            raise ValueError(f"Invalid question type: {question_type}. Must be one of {list(Qtype.__members__.keys())}.")
        compare_questions = self.supabase.table("document").select("*").eq("session_id", self.session_id).eq("subject", subject).eq("question_type", question_type).execute()
        if  len(compare_questions.data) < 2:
            print(f"Not enough questions to compare for subject {subject} and question type {question_type}. Returning None.")
            return None
        compare_questions_all = [f"Question: {q['data']['Question']} Answer: {q['data']['Answer']}" for q in compare_questions.data]
        extracted_questions = extract_questions_eval(file_path)
        print(f"Extracted {len(extracted_questions)} questions from the file.")
        results=[]
        if not extracted_questions:
            print("No questions extracted from the file.")
            return None
        for question in tqdm(extracted_questions):
            QA = str(question)
            results.append(self._majority_vote(QA, subject, question_type, compare_questions_all, k=k))
        if save_results:
            #save as csv
            file_name = os.path.splitext(os.path.basename(file_path))[0]  # Get the file name without extension
            result_file_name = f"eval_{file_name}.csv"
            result_path = os.path.join("output", result_file_name)
            with open(result_path, "w", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Question", "Result", "k"])
                for question, result in zip(extracted_questions, results):
                    writer.writerow([str(question), result, k])
        print(f"Evaluation completed for {len(extracted_questions)} questions.")
        print(sum(results) / len(results) if results else None)

    def _test(self) -> str:
        subject_name = "Operating Systems"
        question_type = "MCQ"
        QA = "What is the main function of an operating system? A) Manage hardware B) Provide user interface C) Execute applications D) All of the above"
        compareQA = [
            "What is the primary role of an operating system? A) Manage resources B) Provide security C) Facilitate communication D) All of the above",
            "What is the main purpose of an operating system? A) Manage hardware B) Provide user interface C) Execute applications D) All of the above"
        ]
        result = self._judge(QA, subject_name, question_type, compareQA)
        print(f"Judgement result: {result}")
        return result
    
if __name__ == "__main__":
    os.environ["AZURE_OPENAI_ENDPOINT"] = "https://hkust.azure-api.net"
    load_dotenv()
    evaluator = Evaluator()
    #the following is for benchmarking 
    evaluator.benchmark(k=1, subject="COMP3511", question_type="MCQ")
    # Uncomment the following line to run the evaluation
    # evaluator.evaluate(
    #     file_path=r"output\questions_v1.0_withPP.json",
    #     subject="COMP3511",
    #     question_type="MCQ",
    #     k=1,
    #     save_results=True
    # )
