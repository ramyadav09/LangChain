import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain_core.documents import Document

# 1. Prepare sample data documents
sample_documents = [
    Document(
        page_content="A Contextual Compression Retriever passes raw documents through a compressor to pull out relevant data."
    ),
    Document(
        page_content="Hugging Face hosts millions of open-source models for NLP, vision, and audio applications."
    ),
    Document(
        page_content="RAG systems combine vector databases with LLMs to ground AI responses in factual context."
    ),
    Document(
        page_content="The weather in Paris today is cloudy with a high of fifteen degrees Celsius."
    ),
    Document(
        page_content="LangChain provides abstractions like document compressors to easily filter out noisy text chunks."
    ),
]

# 2. Build a local Vector Store using Hugging Face Embeddings
# (Requires: pip install langchain-huggingface sentence-transformers faiss-cpu)
embeddings_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vectorstore = FAISS.from_documents(sample_documents, embeddings_model)
base_retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# 3. Initialize the Hugging Face Cross-Encoder model for reranking
# BAAI/bge-reranker-base is highly optimized for filtering relevant context
rerank_model = HuggingFaceCrossEncoder(model_name="BAAI/bge-reranker-base")

# 4. Wrap it in a LangChain Compressor
# top_n=2 means it will only return the 2 highest-scoring matching documents
compressor = CrossEncoderReranker(model=rerank_model, top_n=2)

# 5. Create the Contextual Compression Retriever
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=base_retriever
)

# 6. Run a query to test compression output
query = "How do I compress documents in a LangChain RAG system?"
compressed_docs = compression_retriever.invoke(query)

# 7. Print the results
print(f"--- Query: {query} ---\n")
print(f"Retrieved and compressed to {len(compressed_docs)} documents:\n")
for i, doc in enumerate(compressed_docs):
    print(
        f"[Document {i+1}] Relevance Score: {doc.metadata.get('relevance_score'):.4f}"
    )
    print(f"Content: {doc.page_content}\n")
