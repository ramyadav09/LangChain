import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from langchain.retrievers.multi_query import MultiQueryRetriever
from transformers import pipeline

# 1. Setup Local Embedding Model (Sentence Transformers)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 2. Mock Data & Vector Database Creation
sample_texts = [
    "A Multi-Query Retriever uses an LLM to generate multiple search variations.",
    "RAG systems combine retrieval mechanisms with large language models.",
    "Vector databases store text as high-dimensional embeddings for search.",
    "Hugging Face provides thousands of open-source models for NLP tasks.",
]

vector_db = FAISS.from_texts(sample_texts, embeddings)
base_retriever = vector_db.as_retriever(search_kwargs={"k": 2})

# 3. Setup Local LLM for Generating Query Variations
# Using a lightweight text-generation model
hf_pipeline = pipeline(
    "text-generation",
    model="google/gemma-2b-it",  # Replace with your preferred model
    max_new_tokens=50,
    temperature=0.7,
)
llm = HuggingFacePipeline(pipeline=hf_pipeline)

# 4. Initialize the Multi-Query Retriever
mq_retriever = MultiQueryRetriever.from_llm(retriever=base_retriever, llm=llm)

# 5. Execute the Search
query = "How do multi-query systems work?"
unique_docs = mq_retriever.invoke(input=query)

# 6. Print Results
print(f"\n--- Original Query: {query} ---\n")
print(f"Retrieved {len(unique_docs)} unique documents:\n")
for i, doc in enumerate(unique_docs):
    print(f"Document {i+1}: {doc.page_content}")
