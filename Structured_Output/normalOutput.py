from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

# from typing import TypedDict, Annotated
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

template1 = PromptTemplate(
    template="write a detailed report on {topic}", input_variables=["topic"]
)
template2 = PromptTemplate(
    template="write 5 lines summary of the report.\n {text}", input_variables=["text"]
)


prompt1 = template1.invoke({"topic": "Artificial Intelligence"})
result1 = model.invoke(prompt1)
prompt2 = template2.invoke({"text": result1.content})
result2 = model.invoke(prompt2)
print(result2.content)
