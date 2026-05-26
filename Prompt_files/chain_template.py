import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_openai import ChatOpenAI
from schema.scheam import LLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


quiz_template = PromptTemplate.from_template(
""" Generate 5 Multiple Choice Questions on the topic of {topic} for a {level} student"""
)

chain = quiz_template | LLM | StrOutputParser()

result = chain.invoke({"topic": "Transformers LLM Basics", "level": "Beginner"})
print(result)