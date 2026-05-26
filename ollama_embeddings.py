from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv

load_dotenv(override=True)

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

text = "There is a clash between civilizations and the love between a man and a woman is stronger than the love between a mother and a child."

embedding = embeddings.embed_query(text)
print(embedding)
print(len(embedding))