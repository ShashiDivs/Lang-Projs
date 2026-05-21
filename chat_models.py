from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv(override=True)

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

# response = llm.invoke("What is the capital of Telangana?")
# print(response.content)
# print(response.response_metadata.get("model_name"))

messages = [
    SystemMessage(content="You are an expert in poetry and literature of post modernism."),
    HumanMessage(content="Can you explain about cricket")
]

response = llm.invoke(messages)
print(response.content)