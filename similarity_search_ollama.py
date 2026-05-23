from langchain_ollama import OllamaEmbeddings
import numpy as np
from dotenv import load_dotenv

load_dotenv(override=True)

embeddings = OllamaEmbeddings(
    model="mxbai-embed-large"
)

def cosine_similarity(vec1, vec2):

    v1, v2 = np.array(vec1), np.array(vec2)
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

text = [
    "I love programming in python",
    "Python is my favorite programming language",
    "The weather is nice today",
    "Coding is fun with python"
]

vecc = embeddings.embed_documents(text)
query = "I love programming in python"
query_vector = embeddings.embed_query(query)
query_vector = np.array(query_vector)
for doc, vector in zip(text, vecc):
    similarity = cosine_similarity(query_vector, vector)
    print(f"Document: {doc}")
    print(f"Similarity: {similarity}")
    print("-" * 100)

