from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# The line `# from typing import TypedDict, Annotated` is a commented-out import statement in Python.
# It seems like you were trying to import the `TypedDict` and `Annotated` classes from the `typing`
# module. However, the correct way to import these classes would be:
from typing import TypedDict, Annotated

load_dotenv()


class Movie(TypedDict):
    title: Annotated[str, "The title of the movie"]
    year: Annotated[int, "The release year of the movie"]
    description: Annotated[str, "Description of movie"]


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
structured_result = model.with_structured_output(Movie)
result = structured_result.invoke("Tell me a 5 most famous and good movie of 2026")
print(result)
