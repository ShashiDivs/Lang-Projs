from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
load_dotenv(override=True)

LLM = ChatOpenAI(
    model="gpt-4o-mini"
)

LLM_GROQ = ChatGroq(
    model="llama-3.3-70b-versatile"
)
