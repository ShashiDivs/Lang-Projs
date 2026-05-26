from glob import translate
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from schema.scheam import LLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableSequence

animal_facts_template = ChatPromptTemplate.from_messages([
    ("system", "You love jokes and you tell jokes about {animal}"),
    ("human", "Tell me {count} jokes?")
])

translation_template = ChatPromptTemplate.from_messages([
    ("system", "You are a translation expert convert the provided text into {language}"),
    ("human", "Translate the following text into {language}: {text}")
])



prepare_for_translation = RunnableLambda(lambda output: {"text": output, "language": "Telugu"})

chain = animal_facts_template | LLM | StrOutputParser() | prepare_for_translation | translation_template | LLM | StrOutputParser()

result = chain.invoke({"animal": "cat", "count": 3})
print(result)