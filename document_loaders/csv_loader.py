from langchain_community.document_loaders.csv_loader import CSVLoader
from pathlib import Path
from pprint import pp

file_path = Path("/Users/gaajarlasheshugoud/Desktop/proj-langchain/knowledge-source/organizations.csv")


loader = CSVLoader(file_path=file_path,
                   source_column="Industry",
                   metadata_columns=["Website", "Founded", "Number of employees"],
                   content_columns=["Description"]

)

documents = loader.load()


print(len(documents))

print(documents[0].page_content)


print(documents[0].metadata)