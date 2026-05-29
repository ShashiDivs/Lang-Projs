from langchain_community.document_loaders import WebBaseLoader
from pprint import pp


url_1 = "https://www.iplt20.com/matches/fixtures"
url_2 = "https://www.pinecone.io/"

loader = WebBaseLoader(web_path=[url_1, url_2])


documents = loader.load()

pp(documents[0].page_content)