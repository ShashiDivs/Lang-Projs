from dotenv import load_dotenv
from langchain_openai import OpenAI
from schema.scheam import LLM

# load_dotenv(override=True)

# llm = OpenAI(
#     model="gpt-4o-mini"
# )

print(LLM.invoke("What is the AI revolution?"))
