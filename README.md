
# Results discussion
## questions_v0
- Methodology:
  - Each page is considered a "chunk". For each chunk:
    - the concept is extracted with details, then LLM provides a normal and tricky example
    - another LLM generates questions and answers based on the content 
- Cons:
  - one page per chunk is too short. some pages only contain the title and the LLM end up hallucinating the details, leading to questions that are out of scope. 
  - some questions are generated based on the examples but the examples are not inlcude in the questions. 
- Solution: 
  - chunked according hardcoded length