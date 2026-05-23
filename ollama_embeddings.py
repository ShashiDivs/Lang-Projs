from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv

load_dotenv(override=True)

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

text = "Langchain is a framework for building applications with AI."

embedding = embeddings.embed_query(text)
print(embedding)
print(len(embedding))