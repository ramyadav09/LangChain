from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://news.google.com/home?hl=en-US&gl=US&ceid=US:en")

docs = loader.load()
print(docs.metadata)
