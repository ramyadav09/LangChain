from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# from langchain_community.document_loaders import UnstructuredPDFLoader

loader = PyPDFLoader("../Doc_Loader/ppp.pdf")
docs = loader.load()
# print(docs[0].metadata)
# text = "Because large language models process tokens rather than raw characters, counting characters can sometimes be unpredictable for context window strictness. Token splitters measure length using specific model tokenizers."
splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0, separator="")
result = splitter.split_text(docs[1].page_content)
print(result)
