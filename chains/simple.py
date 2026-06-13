from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()
template = PromptTemplate(
    template="give me a json format output of a movie with name,year and description when i ask for {topic}",
    input_variables=["topic"],
)


chain = template | model | parser
result = chain.invoke({"topic": "Artificial Intelligence"})
print(result)

chain.get_graph().print_ascii()