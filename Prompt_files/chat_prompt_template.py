import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from schema.scheam import LLM
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that specializes in {domain}"),
        ("user", "{user_question}")
    ])


messages = chat_template.format_messages(
    domain="Medicine",
    user_question="What is Oncology and its types?"
)

response = LLM.invoke(messages)
print(response.content)