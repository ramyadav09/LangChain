from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# chat_template = ChatPromptTemplate(
#     [
#         SystemMessage(content="You are a helpful {domain} agent"),
#         HumanMessage(content="Explain in simple terms, what is {topic}"),
#     ]
# )
chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful {domain} agent"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "Explain in simple terms, what is {topic}"),
    ]
)
chat_history = []
with open("chat_history.txt") as f:
    chat_history.append(HumanMessage(content=f.read()))
prompt = chat_template.invoke(
    {"domain": "cricket", "topic": "Dusra", "chat_history": chat_history}
)
print(prompt)
