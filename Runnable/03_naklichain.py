import random


class Naklillm:
    def __init__(self):
        print("Naklillm model initialized.")

    def predict(self, prompt):

        response_list = [
            "Kathmandu is capital of Nepal.",
            "NPL is cricket team of Nepal.",
            "Nepal is a beautiful country.",
        ]
        return {"response": random.choice(response_list)}


# llm = Naklillm()
# prompt = "What is the capital of Nepal?"

# print(llm.predict(prompt))


class NakliPromptTemplate:
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)


template = NakliPromptTemplate(template="What is the capital of {country}?", input_variables=["country"])
# prompt = template.format({"country": "Nepal"})

llm = Naklillm()
# print(llm.predict(prompt))


class NakliLLMChain:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):
        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)
        return result["response"]


chain = NakliLLMChain(llm=llm, prompt=template)
print(chain.run({"country": "Nepal"}))

# This code defines a simple language model (Naklillm) that generates random responses based on a prompt. It also defines a prompt template (NakliPromptTemplate) that can format prompts with input variables. Finally, it defines a chain (NakliLLMChain) that combines the language model and the prompt template to generate responses based on formatted prompts.
#there is a problem we can't create 2 step of chains because the output of one chain is not in the format of input of another chain. We need to modify the code to allow chaining multiple steps together. 