import random
from abc import ABC, abstractmethod


class Runnable(ABC):
    @abstractmethod
    def invoke(input_data):
        pass


class Naklillm(Runnable):
    def __init__(self):
        pass

    def invoke(self, prompt):

        response_list = [
            "Kathmandu is capital of Nepal.",
            "NPL is cricket team of Nepal.",
            "Nepal is a beautiful country.",
        ]
        return {"response": random.choice(response_list)}

    def predict(self, prompt):

        return {"response": "remove this predict method and use invoke method instead"}


class NakliPromptTemplate(Runnable):
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict):
        return self.template.format(**input_dict)

    # def invoke(self, input_dict):
    #     return self.template.format(**input_dict)


class NakliStrOutputParser(Runnable):
    def __init__(self):
        pass

    def invoke(self, input_dict):
        return input_dict["response"]


class RunnableConnector(Runnable):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):
        data = input_data
        for runnable in self.runnable_list:
            data = runnable.invoke(data)
        return data


llm = Naklillm()
parser = NakliStrOutputParser()
# template = NakliPromptTemplate(template="What is the capital of {country}?", input_variables=["country"])
# chain = RunnableConnector([template, llm,parser])
# print(chain.invoke({"country": "Nepal"}))

template1 = NakliPromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

template2 = NakliPromptTemplate(
    template="Explain the following joke {response}", input_variables=["response"]
)

chain1 = RunnableConnector([template1, llm])
# print(chain1.invoke({"topic": "programming"}))

chain2 = RunnableConnector([template2, llm, parser])
# print(chain2.invoke({"response": chain1.invoke({"topic": "programming"})}))

final_chain = RunnableConnector([chain1, chain2])
print(final_chain.invoke({"topic": "programming"}))
