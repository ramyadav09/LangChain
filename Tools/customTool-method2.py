from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


class MultiplyInput(BaseModel):
    a: int = Field(description="First number")
    b: int = Field(description="Second number")


def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


multiply_tool = StructuredTool.from_function(
    func=multiply,
    name="multiply",
    description="Multiply two numbers",
    args_schema=MultiplyInput,
)
res = multiply_tool.invoke({"a": 3, "b": 7})
print(res)
