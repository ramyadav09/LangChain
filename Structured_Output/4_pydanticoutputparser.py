from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


class MovieInfo(BaseModel):
    name: str
    year: int
    description: str


parser = PydanticOutputParser(pydantic_object=MovieInfo)

prompt = PromptTemplate(
    template=" give details of 3 recently released movies \n{format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser

result = chain.invoke({})

print(result)
