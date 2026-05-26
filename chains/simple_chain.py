import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from schema.scheam import LLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert who knows the facts in {topic} "),
    ("human", "Tell me about {sub_topic}?")
])

chain = prompt | LLM | StrOutputParser()

result = chain.invoke({
    "topic": "AI",
    "sub_topic": "AI Agents"
})
print(result)