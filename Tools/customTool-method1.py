from langchain_community.tools import tool


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


res = multiply.invoke({"a": 3, "b": 7})

print(res)
print(multiply.description)
