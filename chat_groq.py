from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv(override=True)

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

messages = [
    SystemMessage(content="You are an expert cook who can suggest recipes based on the ingredients available."),
    HumanMessage(content="Can you suggest a recipe for a chicken curry?")
]

response = llm.invoke(messages)
print(response.content)
