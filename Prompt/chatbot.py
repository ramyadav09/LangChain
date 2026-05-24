from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
chats = []
while True:
    prompt = input("You: ")
    if prompt == "exit":
        break
    chats.append(f"You: {prompt}")
    result = model.invoke(chats)
    chats.append(f"AI: {result.content}")
    print("Response:", result.content)
print(chats)
