from langchain_community.document_loaders import PyPDFLoader
# from langchain_community.document_loaders import UnstructuredPDFLoader

loader = PyPDFLoader("ppp.pdf")
docs = loader.load()
print(docs[1])
print(docs[0].metadata)
