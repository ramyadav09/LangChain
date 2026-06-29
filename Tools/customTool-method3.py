from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class MultiplyInput(BaseModel):
    a: int = Field(description="First number")
    b: int = Field(description="Second number")


class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiply two numbers"
    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a * b


multiply_tool = MultiplyTool()

res = multiply_tool.invoke({"a": 3, "b": 7})
print(res)
