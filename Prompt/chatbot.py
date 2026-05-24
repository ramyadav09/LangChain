from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
chats = [
    SystemMessage(
        content="You are a senior software developer with expertise in Python and JavaScript. You have experience working on large-scale projects and are skilled in problem-solving and debugging."
    ),
]
while True:
    prompt = input("You: ")
    if prompt == "exit":
        break
    chats.append(HumanMessage(content=prompt))
    result = model.invoke(chats)
    chats.append(AIMessage(content=result.content))
    print("Response:", result.content)
print(chats)
