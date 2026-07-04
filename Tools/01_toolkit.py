from langchain_community.tools import tool


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


@tool
def addition(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


class MathToolkit:
    def get_tools(self):
        return [multiply, addition]


toolkit = MathToolkit()
tools = toolkit.get_tools()

for tool in tools:
    print(tool.name)
    print(tool.description)
