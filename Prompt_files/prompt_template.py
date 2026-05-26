import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_openai import ChatOpenAI
from schema.scheam import LLM
from langchain_core.prompts import PromptTemplate


# prompt_template = PromptTemplate(
#     template="What is the capital of {country}?",
#     input_variables=["country"]
# )

# response = llm.invoke(prompt_template.format(country="Argentina"))
# print(response.content)

#Assignment use Input to ask the countries in that user wants to know the capital of.

template = PromptTemplate(
    template="""
    You are an expert in {field}, 
    Explain the concept of '{concept}' in simple terms for a {audience}.
    """
)

prompt = template.format(
    field="AI", 
    concept="AI Stories", 
    audience="children"
)
response = LLM.invoke(prompt)
print(response.content)