from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv(override=True)

LLM = ChatOpenAI(
    model="gpt-4o-mini"
)