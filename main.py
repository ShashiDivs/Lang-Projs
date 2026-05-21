from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv(override=True)

llm = OpenAI(
    model="gpt-4o-mini"
)

print(llm.invoke("What is the AI revolution?"))
