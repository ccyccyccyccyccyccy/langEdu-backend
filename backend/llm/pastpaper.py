import os
import asyncio
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from enum import Enum
from typing import Optional, List, Tuple

from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, Field
from langchain.schema import BaseCache, LLMResult
from langchain_core.output_parsers import StrOutputParser
import json
from supabase import create_client, Client

from utils import parse_pdf, get_hf_embeddings
from db import *
from user import get_client_session, get_supabase

class Qtype(str, Enum):
    MCQ = "MCQ"
    ShortAnswer = "Short Answer"
    LongAnswer = "Long Answer"
    Coding = "Coding"
    Numerical = "Numerical"
    Others = "Others"

class PastpaperQ(BaseModel):
    """Information about a past paper question."""
    question: str = Field(
        description="The question text from the past paper"
    )
    answer: Optional[str] = Field(default=None, description="Answer to the question extracted from the document")
    topic: str = Field(
        description="Fine-grained topic of the question, e.g.'Capitals of countries' in Geography"
    )
    question_type: str = Field(
        description="Type of question, e.g. 'MCQ', 'Short Answer', etc."
    )
    def __str__(self):
        return f"Question: {self.question}, Answer: {self.answer}, Topic: {self.topic}, Type: {self.question_type}"
    
class ExtractionData(BaseModel):
    """Extracted information about questions in pastpaper documents."""
    questions: List[PastpaperQ]

# Function to extract PP questions
def extract_questions(text):  # Input: List of langchain docs
    # Define a custom prompt to provide instructions and any additional context
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert at extracting key information about a question in pastpapers. "
                "Irrelevant content may be present e.g. table of contents. Ignore the content if it is not a question."
                "When extracting a question, please ensure to include the COMPLETE question text, including possible options for MCQs, if any"
                "Extract the complete question, its answer, the topic it belongs to, and deduce type of question. Leave the answer blank if it is not available in the document. ",
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
        [{"text": t} for t in text], #t is of the type Document
        {"max_concurrency": 5},  # Limit concurrency
    )

    # Collect extracted key concepts
    all_questions = []
    for extraction in extractions:
        all_questions.extend(extraction.questions)

    return all_questions

def validate_extraction(extracted_questions):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a judge judging questions from past papers. "
                "Determine if the provided question adheres to an answerable format. Incomplete questions are not answerable."
                "For MC questions, ensure that the question includes all options."
                "Reply ONLY 'yes' if the question is answerable, otherwise reply 'no'.",
            ),
            ("human", "{text}"),
        ]
    )

    # Instantiate the AzureChatOpenAI model
    
    llm = AzureChatOpenAI(
        azure_deployment="gpt-4o",  # Replace with your deployment
        api_version="2025-02-01-preview",  # Replace with your API version
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    chain = prompt | llm | StrOutputParser()
    valid_questions=[]
    for question in extracted_questions:
        text = question.question
        response = chain.invoke({"text": text})
        if "yes" in response.lower():
            valid_questions.append(question)
        else:
            print(f"Invalid question: {question}")
    return valid_questions
    
def insert_valid_questions(supabase, valid_questions, subject):
    session_id = get_client_session()
    hf = get_hf_embeddings()
    for question in valid_questions:
        data= {"Question": question.question, "Answer": question.answer}
        binary = json.dumps(data).encode('utf-8')
        insert_document(supabase, hf, binary, subject=subject, topic=question.topic, question_type=question.question_type, session_id=session_id)
    print("Successfully inserted valid questions into the database.")
        
    
if __name__ == "__main__":
   load_dotenv()
   supabase = get_supabase()
   os.environ["AZURE_OPENAI_ENDPOINT"] = "https://hkust.azure-api.net"
   docs= asyncio.run(parse_pdf(r"data\comp3511_f2024_midterm_solution.pdf"))
   print(len(docs))
   questions = extract_questions(docs[:5])
   for q in questions:
        print(q)
   valid_questions = validate_extraction(questions)
   print(f"Valid questions: {len(valid_questions)}")
   insert_valid_questions(supabase, valid_questions, subject="COMP3511")
        
   