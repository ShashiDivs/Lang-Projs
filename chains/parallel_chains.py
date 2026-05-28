from glob import translate
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from schema.scheam import LLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel

# step 1 Get a movie summary
summary_chain = (
    ChatPromptTemplate.from_messages([
        ("system","You are movie critic"),
        ("human","Please provide a summary of the movie {movie_name}?")
    ]) 
    | LLM
    | StrOutputParser()
)

parallel_chain = RunnableParallel(
    plot = (
        ChatPromptTemplate.from_messages([
        ("system","You are movie critic"),
        ("human","Analze the plot of this movie: {input}. strength and weaknesses?")
    ])
    | LLM
    | StrOutputParser()
   ),
    characters = (
        ChatPromptTemplate.from_messages([
        ("system","You are movie critic"),
        ("human","Analyze the characters in the movie summary: {input}. strengths and weaknesses?")
    ])
    | LLM
    | StrOutputParser()
   )
)


full_chain = (
    summary_chain
    | RunnableLambda(lambda summary: {"input": summary})
    | parallel_chain
    | RunnableLambda(lambda x: f"Plot Analysis: \n{x['plot']}\n\nCharacters Analysis: \n{x['characters']}")
)

#result = full_chain.invoke({"movie_name": "Akhanda"})
#print(result)

# streaming we use streaming to reduce the latency and improve the user experience
for chunk in full_chain.stream({"movie_name": "Jalsa"}):
    print(chunk, end="", flush=True)