# Code explanation

## v0.1

- Note: sorry for changing the file paths again. I wasn't using VSCode before and the file paths were interpreted differently. Now they should work on vscode. Simply run test.py, and the output in the terminal should be something like: 

```
20
{'producer': 'Adobe PDF Library 20.6.66', 'creator': 'Acrobat PDFMaker 20 for PowerPoint', 'creationdate': '2024-10-26T08:38:42+08:00', 'author': 'Designed by Slidesmash', 'moddate': '2025-05-31T22:48:47+08:00', 'title': 'Designed by Slidesmash', 'source': 'data\\COMP4521_L6 - Data Management on Cloud.pdf', 'total_pages': 20, 'page': '0-7', 'page_label': '1'}
{'producer': 'Adobe PDF Library 20.6.66', 'creator': 'Acrobat PDFMaker 20 for PowerPoint', 'creationdate': '2024-10-26T08:38:42+08:00', 'author': 'Designed by Slidesmash', 'moddate': '2025-05-31T22:48:47+08:00', 'title': 'Designed by Slidesmash', 'source': 'data\\COMP4521_L6 - Data Management on Cloud.pdf', 'total_pages': 20, 'page': '8-11', 'page_label': '9'}
...
Title: Firebase, Details: A comprehensive platform developed by Google that provides a variety of tools and services to help developers build and manage mobile and web applications.
Title: Realtime Database, Details: A NoSQL cloud database that allows data to be stored as JSON and synchronized in real-time across all clients, supporting CRUD operations.
...
========================================
Questions saved to output\questions_v0.1.json
```
- the terminal output is not important. The important output is saved in the json file under the output directory. 
- Code explananations:
    - the pdf is parsed and read into LangChain [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html) objects. 
    - from the Document objects, the LLM extracts the information into a common format. This is an [extraction chain](https://python.langchain.com/docs/tutorials/extraction/). The first time, we extract the information into Concept objects (defined by the Concept class), from there we ask the LLM to generate Examples and finally Questions. 
    - also drawing reference from [this] (https://python.langchain.com/docs/how_to/extraction_long_text/)
    - the lines
    ```
    llm = AzureChatOpenAI(
        azure_deployment="gpt-4o-mini",  # Replace with your deployment
        api_version="2024-10-01-preview",  # Replace with your API version
        temperature=0.1,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    ```
    defines the API model version we are using.
    - Footnotes:
        - SimpleCache class is useless. We just add it because Pydantic syntax requires it. 

## v1: integrate PP with the Supabase database
### Setup
- To initiate a client instance to the created DB, add the following variables to your .env file: ```SUPABASE_URL``` , ```SUPABASE_KEY```
- Moreover, each client instance can only access rows with the same session id. If the ```SESSION_ID``` variable is not supplied in the .env file, a new one will automatically be created. For development purposes, you may find it more convenient to keep using the same session id (so you can view all your previous uploaded documents). To do that, run ```user.py```, copy the printed session id and paste it into your .env file. 
### DB functions: described in db.py
- main functions of interest: ```insert_document```, ```query_pp_by_topic```, ```delete_data_by_session```
- read the doc strings and the tests for usage examples. 
### Inserting PP documents into the DB
- Example script shown in ```pastpaper.py```
- Parameters to change are under the main section: 
```docs= asyncio.run(parse_pdf(r"data\comp3511_f2024_midterm_solution.pdf"))```
```insert_valid_questions(supabase, valid_questions, subject="COMP3511")```
### Integration of PP into test.py
- Main changes, under the main section:
- ```pp_questions = query_pp("COMP3511", result)```
- Changing the subject to ```None``` means the subject filter is not imposed. 
### Evaluation script
- see ```evaluate.py```
- Read the ```discussions.md``` to understand how the evaluation works first. 
- ```evaluator.benchmark``` performs benchmarking with real PP questions. To do your own benchmarking, change the hardcoded values the ```subject``` and ```question_types``` inside the function. Otherwise, just refer to the values in ```discussion.md``
- ```evaluator.evaluate``` is the main evaluation function. It evaluates the quality of questions after the json file has been generated from ```test.py```. If ```save_results``` has been set to True, a csv file will be saved in output/ . It contains the questions, the scores for each question, and the value of k used. For each question, the closer its score is to 1, the more different it is from authentic Qs. 

