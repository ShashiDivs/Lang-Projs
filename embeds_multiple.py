from zipimport import zipimporter
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv(override=True)

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

documents = [
    "Langchain is a framework for building applications with AI.",
    "AI is the future of programming.",
    "Transformers are a type of neural network architecture.",
    "Generative Pre-trained Transformer (GPT) is a type of transformer model."
]

doc_vectors = embeddings.embed_documents(documents)

for doc, vector in zip(documents, doc_vectors):
    print(f"Document: {doc}")
    print(f"Vector: {vector}")
    print("-" * 100)

print(len(doc_vectors))
print(len(doc_vectors[0]))