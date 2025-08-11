
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

## Evaluation
- Implentation: 
  - we group the generated question with 2 other real PP questions of the same subject and question type, and ask a judge LLM (default gpt-4o) to choose the odd one out among the group in terms of question quality and depth. This process can be repeated for k times and the results will be averaged, where k is a parameter. 
- to eliminate the effects of position bias, or any other unintended effects, we benchmark this scoring method on real PP Questions. for 
  -  benchmark results: 
  - k= 1: 0.04761
  - k= 5: 0.02857
  - in other words, as the quality of generated questions approach the authentic PP questions, we expect the score to be close to the above benchmarks
- The results of output\questions_V1.0_withPP.json with k=1: 0.1136