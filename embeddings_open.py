from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv(override=True)

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

text = "Langchain is a framework for building applications with AI."

embedding = embeddings.embed_query(text)
#print(embedding)
print(len(embedding))