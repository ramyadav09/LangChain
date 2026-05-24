from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
result = model.invoke("Tell me a 5 most famous and good movie of 2026")
print(result.content)
