from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


class Movie(BaseModel):
    title: str = Field(..., description="The title of the movie")
    year: int = Field(..., description="The release year of the movie")
    description: str = Field(..., description="Description of movie")


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
structured_result = model.with_structured_output(Movie)
result = structured_result.invoke("Tell me a 5 most famous and good movie of 2026")
print(result.title)
print(result.year)
print(result.description)
