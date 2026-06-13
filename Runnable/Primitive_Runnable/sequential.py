from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(dotenv_path=r"C:\Users\KIIT\OneDrive\Desktop\GenAI\.env")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()
prompt1 = PromptTemplate(
    template="generate a detailed report on topic\n {topic}",
    input_variables=["topic"],
)
prompt2 = PromptTemplate(
    template="generate 5 pointer summary in the given text\n {text}",
    input_variables=["text"],
)

chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({"topic": "Artificial Intelligence"})
print(result)

chain.get_graph().print_ascii()
