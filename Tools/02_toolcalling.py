from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain.messages import HumanMessage

load_dotenv()

query = HumanMessage("multiply 5 and 10")
messages = [query]


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers and return its result"""
    return a * b


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
# Tool Binding with LLM
tool_with_llm = llm.bind_tools([multiply])

# Tool calling
res = tool_with_llm.invoke(messages)
# print(res.tool_calls)
messages.append(res)
# Tool Execution

tool_result = multiply.invoke(res.tool_calls[0])
# print(tool_result)

messages.append(tool_result)
# print(messages)

result = tool_with_llm.invoke(messages)
print(result.content)
