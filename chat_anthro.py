from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv(override=True)

llm = ChatAnthropic(
    model="claude-haiku-4-5-20251001"
)

# response = llm.invoke("What is the capital of Telangana?")
# print(response.content)
# print(response.response_metadata.get("model_name"))

messages = [
    SystemMessage(content="You are an expert cook who can suggest recipes based on the ingredients available."),
    HumanMessage(content="Can you suggest a recipe for a chicken curry?")
]

response = llm.invoke(messages)
print(response.content)