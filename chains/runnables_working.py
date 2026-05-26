import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from schema.scheam import LLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableSequence

prompt = ChatPromptTemplate.from_messages([
    ("system", "You love facts and you tell facts about {animal}"),
    ("human", "Tell me {count} facts?")
])


format_prompt = RunnableLambda(lambda x: prompt.format_messages(**x))
invoke_llm = RunnableLambda(lambda x: LLM.invoke(x))
parse_output = RunnableLambda(lambda x: x.content)


chain = RunnableSequence(format_prompt, invoke_llm, parse_output)

result = chain.invoke({"animal": "cat", "count": 3})
print(result)