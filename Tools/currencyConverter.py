# It is nor a Agent, it is a tool that can be used by an agent to convert currency. It uses the Exchange Rate API to get the current exchange rate between two currencies and then uses that rate to convert an amount from one currency to another.

import os
import requests
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


@tool
def convert_currency(from_currency: str, to_currency: str) -> float:
    """Get the current exchange rate to convert from one currency to another."""
    api_key = os.getenv("EXCHANGE_RATE_API_KEY")
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}"
    response = requests.get(url)
    data = response.json()
    return data["conversion_rate"]


@tool
def convert(base_currency_value: float, conversion_rate: float) -> float:
    """Convert an amount from one currency to another using a given conversion rate."""
    return base_currency_value * conversion_rate


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
llm_with_tools = llm.bind_tools([convert_currency, convert])
query = "What is the conversion factor between USD and INR, and based on that can you convert 10 usd to inr"
messages = [HumanMessage(query)]

tool_map = {"convert_currency": convert_currency, "convert": convert}

ai_message = llm_with_tools.invoke(messages)
messages.append(ai_message)

# Loop until the model stops requesting tool calls (it needs two rounds here:
# one to get the rate, one to do the multiplication with that rate)
while ai_message.tool_calls:
    for tool_call in ai_message.tool_calls:
        selected_tool = tool_map[tool_call["name"]]
        tool_output = selected_tool.invoke(tool_call["args"])
        messages.append(
            ToolMessage(content=str(tool_output), tool_call_id=tool_call["id"])
        )

    ai_message = llm_with_tools.invoke(messages)
    messages.append(ai_message)

print(ai_message.content)
