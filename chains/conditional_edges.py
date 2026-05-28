from glob import translate
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from schema.scheam import LLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch

templates = {
    "positive":"Generate a thank you note for this positive feedback: {feedback}",
    "negative":"Generate a response addressing this negative feedback: {feedback}",
    "neutral":"Generate a request for more details for this neutral feedback: {feedback}",
    "escalate":"Generate a message to escalate feedback to human agent: {feedback}",
}


def make_chain(key):
    return (
        ChatPromptTemplate.from_messages([
        ("system","You are a helpful assistant."),
        ("human",templates[key]),
        ])
        | LLM
        | StrOutputParser()
    )

branches = RunnableBranch(
    (lambda x: "positive" in x, make_chain("positive")),
    (lambda x: "negative" in x, make_chain("negative")),
    (lambda x: "neutral" in x, make_chain("neutral")),
    make_chain("escalate")
)

classification_chain = (
    ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("human", "Classify the sentiment of this feedback as positive, negative, neutral or escalte: {feedback}")
    ])
    | LLM
    | StrOutputParser()
)


chain = classification_chain | branches


review = "The product is good. It works really well and I am so happy to purchased this and i would recommend this to everyone."


result  = chain.invoke({"feedback":review})

print(result)


#pydantic structured output