from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = JsonOutputParser()
template = PromptTemplate(
    template="give me a json format output of a movie with name,year and description when i ask for {topic}\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# prompt = template.invoke({"topic": "the most famous and good movie of 2026"})
# result = model.invoke(prompt)
# print(result.content)
# final_result = parser.parse(result.content)
# print(final_result)


chain = template | model | parser
result = chain.invoke({"topic": "Artificial Intelligence"})
print(result)


