import os
import asyncio
from dotenv import load_dotenv
from typing import Optional, List, Tuple

from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, Field
from langchain.schema import BaseCache, LLMResult
from langchain_core.output_parsers import StrOutputParser
import json

from utils import parse_pdf

class Concept(BaseModel):
    """Information about a concept."""

    # ^ Doc-string for the entity Concept.
    # This doc-string is sent to the LLM as the description of the schema Concept,
    # and it can help to improve extraction results.

    # Note that:
    # 1. Each field is an `optional` -- this allows the model to decline to extract it!
    # 2. Each field has a `description` -- this description is used by the LLM.
    # Having a good description can help improve extraction results.
    title: Optional[str] = Field(default=None, description="One sentence description of the concept")
    details: Optional[str] = Field(
        default=None, description="A detailed description of the concept"
    )
    def __str__(self):
        return f"Title: {self.title}, Details: {self.details}"
   
class Examples(BaseModel):
    typical_example: str = Field(
        default=None, description="A typical example of the concept"
    )
    tricky_example: str = Field(
        default=None, description="A tricky example of the concept")
    def __str__(self):
        return f"Typical Example: {self.typical_example}, Tricky Example: {self.tricky_example}"
    
class Questions(BaseModel):
    questions: Optional[str] = Field(
        default=None, description="Questions-answer pairs."
    )
    



class ExtractionData(BaseModel):
    """Extracted information about key concepts from lecture materials."""

    keyConcepts: List[Concept]

class GenerateExamples(BaseModel):
    """Generated examples for a concept."""

    examples: List[Examples]

class GenerateQuestions(BaseModel):
    """Generated questions for a concept."""

    questions: List[Questions]

# Define a minimal BaseCache implementation
class SimpleCache(BaseCache):
    """A basic cache implementation."""
    def lookup(self, key: str):
        return None  # No caching implemented

    def update(self, key: str, value: str):
        pass  # No caching implemented

def combine_docs(old_docs, max_size):
    combined_docs=[]
    current_end_page=0

    while old_docs:
        first_doc= old_docs[0]
        current_start_page = first_doc.metadata['page']
        current_content = ""
        current_counter=0 #how many docs away from first doc
        while (len(current_content.split(' '))<max_size and current_counter<len(old_docs)): #the number of words is smaller than max size
            current_content += old_docs[current_counter].page_content
            current_end_page = old_docs[current_counter].metadata['page']
            current_counter+=1
        #make a new document
        new_doc =  Document(
    page_content= current_content,
    metadata=first_doc.metadata #keep all other fields of metadata
)
        new_doc.metadata['page']= str(current_start_page) + "-" + str(current_end_page)
        combined_docs.append(new_doc)
        #remove the old docs which have been processed
        old_docs= old_docs[current_counter:]
    return combined_docs







# Function to extract concepts
def extract_concept(text):  # Input: List of langchain docs
    # Define a custom prompt to provide instructions and any additional context
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert at identifying key concepts in text. "
                "Only extract important concepts. Extract nothing if no important information can be found in the text.",
            ),
            ("human", "{text}"),
        ]
    )

    # Instantiate the AzureChatOpenAI model
    
    llm = AzureChatOpenAI(
        azure_deployment="gpt-4o-mini",  # Replace with your deployment
        api_version="2024-10-01-preview",  # Replace with your API version
        temperature=0.1,
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
    key_concepts = []
    for extraction in extractions:
        key_concepts.extend(extraction.keyConcepts)

    return key_concepts

def generate_examples(concepts:List[Concept]):  # Input: List of langchain docs
    # Define a custom prompt to provide instructions and any additional context
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert at illustrating concepts with detailed examples. "
                "Generate detailed examples for the given concept.",
            ),
            ("human", "{text}"),
        ]
    )

    # Instantiate the AzureChatOpenAI model
    
    llm = AzureChatOpenAI(
        azure_deployment="gpt-4o-mini",  # Replace with your deployment
        api_version="2024-10-01-preview",  # Replace with your API version
        temperature=0.1,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    
    # Rebuild the model to finalize it
    AzureChatOpenAI.model_rebuild()

    # Create an extractor with structured output
    generator = prompt | llm.with_structured_output(
        schema=GenerateExamples,
        include_raw=False,
    )

    # Process the first few texts
    concepts_string = [str(concept) for concept in concepts]
    generations = generator.batch(
        [{"text": t} for t in concepts_string],
        {"max_concurrency": 5},  # Limit concurrency
    )

    # Collect extracted key concepts
    examples = []
    for ex in generations:
        examples.extend(ex.examples)

    return examples

def getQuestionPrompt(question_type, mustInstrutions, mayInstructions): # change of inputs (add one input: question_type)
    # Define a custom prompt to provide instructions and any additional context
    
    # changes_start:
    # question_type = input("A: MCQ\nB: True or False\nC:Long question\nWhich type of question do you want?")
    example = ""
    if question_type == 'Multiple choice question':
        example = "multiple choice questions: Question: What is the capital of France? a) Paris b) London c) Berlin d) Madrid. Answer: a) Paris"
    elif question_type == 'True or False question':
        example = "true or false questions: Question: The sun rises in the west and sets in the east.True or false?  Answer: False."
    elif question_type == 'Long question':
        example = "long questions: Question: Explain how a hash function maps keys to array indices in a hash table. Why is the modulo operation commonly used in hash functions? Answer: A hash function converts keys (e.g., integers, strings) into indices within a fixed-size array (hash table). The modulo operation (key % table_size) ensures the output fits within the table bounds."
    # changes_end

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert at generating to questions to test students' understanding of concepts."
                "You may use the examples to generate questions that are relevant to the concept. You may skip the questions if you think the given content is not enough to generate questions."
                "You may refer to the sample questions, if any, to generate questions."
                f"The questions MUST {mustInstrutions}"
                f"The questions MAY {mayInstructions}"
            ),
            ("human", 
             f"The questions MUST {mustInstrutions}"
             f"The questions MAY {mayInstructions}"
             f"Example questions for {example}" # a small change
             "Concept: {concept}, Examples: {examples}, Sample Questions: {pp_questions}, "
            )
        ]
    )
    return prompt

# change of input (add one input: question_type)
def generate_questions(concepts:List[Concept], examples:List[Examples], ppQuestions, question_type, mustInstrutions, mayInstructions):  # Input: List of langchain docs
    
    def stringify_questions_list(questions):
        """
        Convert a list of questions to a string.
        """
        lines = []
        for q in questions:
            data = q["data"]
            # Ensure data is a string, decode if it's bytes
            if isinstance(data, bytes):
                data = data.decode('utf-8')
                try:
                    data = json.loads(data)
                except Exception:
                    pass
                if isinstance(data, dict):
                    question = data.get("Question", "")
                    answer = data.get("Answer", "")
                    lines.append(f"Question: {question}, Answer: {answer}")
                else:
                    lines.append(str(data))
        return "\n".join(lines)
    
    # Define a custom prompt to provide instructions and any additional context
    prompt = getQuestionPrompt(question_type, mustInstrutions, mayInstructions)

    # Instantiate the AzureChatOpenAI model
    
    llm = AzureChatOpenAI(
        azure_deployment="gpt-4o-mini",  # Replace with your deployment
        api_version="2024-10-01-preview",  # Replace with your API version
        temperature=0.1,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    
    # Rebuild the model to finalize it
    AzureChatOpenAI.model_rebuild()

    chain = prompt | llm | StrOutputParser()
    

    # Process the first few texts
    concepts= [concept.title for concept in concepts]
    examples = [str(example) for example in examples]
    pp_questions = [stringify_questions_list(qList) for qList in ppQuestions]  # Convert ppQuestions to string if needed
    # Prepare the batch input
    inputs = [{"concept": c, "examples": e, "pp_questions": q} for c, e, q in zip(concepts, examples, pp_questions)]
    print(inputs)
   # Invoke the chain in batch mode
    generations = chain.batch(inputs)

    # Extract generated questions
    questions = [gen for gen in generations]
    return concepts, questions

def query_pp(subject:str, concepts):
    """
    Query past paper questions by subject and concepts.
    Returns a list of lists of questions.
    """
    from db import query_by_topic, query_pp_by_topic
    from user import get_client_session, get_supabase
    from utils import get_hf_embeddings
    supabase = get_supabase()
    hf = get_hf_embeddings()
    questions = [] # list of lists of documents 
    for concept in concepts:
        topic_name = concept.title
        topic_id = query_by_topic(supabase, topic_name, subject, hf)
        results = query_pp_by_topic(supabase, topic_id, subject)
        questions.append(results)
    return questions
    


if __name__ == "__main__":
   load_dotenv()
   os.environ["AZURE_OPENAI_ENDPOINT"] = "https://hkust.azure-api.net"
   docs= asyncio.run(parse_pdf(r"data\Chapter4.pdf"))
   print(len(docs))
   combined_docs= combine_docs(docs, 100)[:3] #just get the first 10 documents for testing
#    for i in range(len(combined_docs)):
#         print(combined_docs[i].metadata)
#    print("========================================")

   result= extract_concept(combined_docs)
   print(f"Extracted {len(result)} concepts.")
   pp_questions = query_pp("COMP3511", result)
#    for q, c in zip(pp_questions, result):
#     print(f"Concept: {c.title}")
#     print(f"Number of pp questions: {len(q)}")
#     for question in q:
#         print(question["topic"])
              

#    for i in range(len(result)):
#     print(result[i])
   print("========================================")
   examples = generate_examples(result)
#    for i in range(len(examples)):
#     print(examples[i])
#    print("========================================")
   question_type = input("Multiple choice question / True or False question / Long question? Which type of question do you want?")
   concepts, questions = generate_questions(result, examples, pp_questions, question_type, f"be {question_type}", "include calculations or code snippets if relevant")
#    for i in range(len(questions)):
#     print(questions[i])
   json_data = {
        "content": [],
    }
   for c, q in zip(concepts, questions):
    json_data["content"].append({
        "concept": c,
        "questions": q,
    })
    # Convert the dictionary to a JSON string
   json_string = json.dumps(json_data, indent=4)
# Write the JSON string to a file
   file_path = "output\questions_3511.json"
   with open(file_path, "w") as json_file:
    json_file.write(json_string)
    print(f"Questions saved to {file_path}")



   



