from dotenv import load_dotenv
#from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv(override=True)

# llm = ChatOpenAI(
#     model="gpt-4o-mini"
# )
llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# response = llm.invoke("What is the capital of Telangana?")
# print(response.content)
# print(response.response_metadata.get("model_name"))

messages = [
    SystemMessage(content="You are an expert in science."),
    HumanMessage(content="What is gravity?"),
    AIMessage(content="Gravity is the force of attraction between two objects with mass."),
    HumanMessage(content="What causes gravity?")
]

response = llm.invoke(messages)
print(response.content)