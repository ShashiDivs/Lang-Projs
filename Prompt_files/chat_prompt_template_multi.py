import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from schema.scheam import LLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import MessagesPlaceholder



multi_turn_template = ChatPromptTemplate.from_messages([
    ("system","You are a freindly Python tutor who helps students learn programming."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{user_input}")
])

history = [
    HumanMessage(content="What is a tuple in Python?"),
    AIMessage(content="A tuple is an immutable sequence of objects. Example: ('apple', 'banana', 'cherry')"),
    HumanMessage(content="How do I add elements to a tuple?"),
    AIMessage(content="Use .append() method to add elements to a tuple."),
]

chain = multi_turn_template | LLM | StrOutputParser()

result = chain.invoke({
    "chat_history": history,
    "user_input": "How does it used in java?"
})
print(result)

