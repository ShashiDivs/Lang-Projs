import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_openai import ChatOpenAI
from schema.scheam import LLM
from langchain_core.prompts import PromptTemplate


code_review_template = PromptTemplate.from_template("""
You are a senior {language} developer.
You are given a code snippet and you need to review it and provide a detailed report on the code.
Review the following code and provide:
1. Issues found
2. Suggestions for improvement
3. Overall code quality
4. Performance issues
5. Security issues
6. Best practices
7. Code readability
8. Code maintainability
9. Code efficiency
10. Code scalability


Code:
```{language}
{code}
```
""")

simple_code = """
def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number
"""

prompt = code_review_template.format(
    language="Python",
    code=simple_code
)

response = LLM.invoke(prompt)
print(response.content)