import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from schema.scheam import LLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

persona_template = ChatPromptTemplate.from_messages([
    ("system","""
    You are {persona_name}, a {persona_role},
    Your communication style is {style},
    Always resposd in chracter
    """),
    ("human", "{question}")
])

chain = persona_template | LLM | StrOutputParser()

response = chain.invoke({
    "persona_name": "Shashi",
    "persona_role": "Poet",
    "style": "Post-Modernism",
    "question": "How to write a poem on the topic of AI?"
})
print(response)