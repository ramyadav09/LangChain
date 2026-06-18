from langchain_text_splitters import RecursiveCharacterTextSplitter

text = "Because large language models process tokens rather than raw characters, counting characters can sometimes be unpredictable for context window strictness. Token splitters measure length using specific model tokenizers."
splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=0)
result = splitter.split_text(text)
print(result)
