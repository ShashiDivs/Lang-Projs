from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv(override=True)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = "Langchain is a framework for building applications with AI."

embedding = embeddings.embed_query(text)
print(embedding)
print(len(embedding))