import os
import asyncio
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from typing import Optional, List, Tuple

from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, Field
from langchain.schema import BaseCache, LLMResult
from langchain_core.output_parsers import StrOutputParser
import json

class Concept(BaseModel):
    """Information about a concept."""

    # ^ Doc-string for the entity Person.
    # This doc-string is sent to the LLM as the description of the schema Person,
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
    """
    typical_example: Optional[str] = Field(
        default=None, description="A typical example of the concept"
    )
    tricky_example: Optional[str] = Field(
        default=None, description="A tricky example of the concept"
    )
    code_sample: Optional[str] = Field(
        default=None, description="A code sample that illustrates the concept"
    )
    questions: Optional[str] = Field(
        default=None, description="Questions testing the concept"
    )
    """
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
    """
    answers: Optional[str] = Field(
        default=None, description="Ground truth answers to the question"
    )
    """



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

def getQuestionPrompt(mustInstrutions, mayInstructions):
    # Define a custom prompt to provide instructions and any additional context
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert at generating to questions to test students' understanding of concepts."
                "You may use the examples to generate questions that are relevant to the concept. You may skip the questions if you think the given content is not enough to generate questions."
                f"The questions MUST {mustInstrutions}"
                f"The questions MAY {mayInstructions}"
            ),
            ("human", 
             f"The questions MUST {mustInstrutions}"
             f"The questions MAY {mayInstructions}"
             "Example questions for multiple choice questions: Question: What is the capital of France? a) Paris b) London c) Berlin d) Madrid. Answer: a) Paris"
             "Concept: {concept}, Examples: {examples}"
            )
        ]
    )
    return prompt

def generate_questions(concepts:List[Concept], examples:List[Examples],mustInstrutions, mayInstructions):  # Input: List of langchain docs
    # Define a custom prompt to provide instructions and any additional context
    prompt = getQuestionPrompt(mustInstrutions, mayInstructions)

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
    # Prepare the batch input
    inputs = [{"concept": c, "examples": e} for c, e in zip(concepts, examples)]

   # Invoke the chain in batch mode
    generations = chain.batch(inputs)

    # Extract generated questions
    questions = [gen for gen in generations]
    return concepts, questions
    

async def parse_pdf(path): #return 

    loader = PyPDFLoader(path)
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)
    return pages

if __name__ == "__main__":
   print(os.getcwd())
   load_dotenv()
   os.environ["AZURE_OPENAI_ENDPOINT"] = "https://hkust.azure-api.net"
   docs= asyncio.run(parse_pdf(r"../../data/COMP4521_L6 - Data Management on Cloud.pdf"))
   print(len(docs))
   combined_docs= combine_docs(docs, 100)
   for i in range(len(combined_docs)):
        print(combined_docs[i].metadata)
#    print("========================================")

   result= extract_concept(combined_docs)

   for i in range(len(result)):
    print(result[i])
   print("========================================")
   examples = generate_examples(result)
#    for i in range(len(examples)):
#     print(examples[i])
#    print("========================================")
   concepts, questions = generate_questions(result, examples, "be multiple choice questions", "include code snippets")
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
   with open("../../output/questions_v0.1.json", "w") as json_file:
    json_file.write(json_string)


   



