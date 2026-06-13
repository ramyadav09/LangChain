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
    def __init__(self,template,input_variables):
        self.template=template
        self.input_variables=input_variables
        
    def format(self,input_dict):
       return self.template.format(**input_dict)

template="What is the capital of {country}?"
input_variables=['country']
template = NakliPromptTemplate(template=template, input_variables=input_variables)
prompt=template.format({"country": "Nepal"})

llm=Naklillm()
print(llm.predict(prompt))
