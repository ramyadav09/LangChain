from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()
result = search_tool.invoke("What is the weather in London?")
print(result)
print(search_tool.description)
