from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv(override=True)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite"
)

messages = [
    SystemMessage(content="You are an expert cook who can suggest recipes based on the ingredients available."),
    HumanMessage(content="Can you suggest a recipe for a chicken curry?")
]

response = llm.invoke(messages)
print(response.content)
