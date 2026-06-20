import wikipedia
wikipedia.set_user_agent("MyLangChainApp/1.0")

from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=2)
query = "What is npm?"
docs = retriever.invoke(query)
print(docs[0].page_content[:500])
