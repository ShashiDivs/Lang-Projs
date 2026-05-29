from langchain_community.document_loaders import TextLoader
from pathlib import Path
from pprint import pp


file_path = Path(__file__).parent.parent / "knowledge-source/transformers.txt"

loader = TextLoader(file_path=file_path, encoding="cp1252")

documents = loader.load()

pp(documents)