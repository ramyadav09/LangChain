from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

schemas = [
    ResponseSchema(name="name", description="name of the movie"),
    ResponseSchema(name="year", description="year of release"),
    ResponseSchema(name="description", description="short movie description"),
]

parser = StructuredOutputParser.from_response_schemas(schemas)

prompt = PromptTemplate(
    template="""
Provide information about the movie "{movie}".

{format_instructions}
""",
    input_variables=["movie"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser

result = chain.invoke({"movie": "A.I. Artificial Intelligence"})

print(result)
