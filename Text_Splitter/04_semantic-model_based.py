from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv

load_dotenv()
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")


# Create the semantic splitter instance
text_splitter = SemanticChunker(
    embeddings=embeddings,
    breakpoint_threshold_type="percentile",  # Type of threshold used to split
    breakpoint_threshold_amount=85.0,  # Splitting sensitivity parameter
)

# Your target continuous text block
sample_text = """
    Neural networks are computational models inspired by the human brain. 
    They consist of interconnected nodes that process information in layers. 
    In business, managing cash flow is critical for maintaining liquidity. 
    Companies must carefully balance their accounts receivable and payable to stay solvent."""

# Split into documents
docs = text_splitter.create_documents([sample_text])


print(docs)
