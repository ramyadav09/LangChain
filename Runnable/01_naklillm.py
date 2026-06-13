import random
class Naklillm:
    def __init__(self):
        print("Naklillm model initialized.")

    def generate_text(self, prompt):
        
        response_list=['Kathmandu is capital of Nepal.','NPL is cricket team of Nepal.','Nepal is a beautiful country.']
        return {'response': random.choice(response_list)}
    

llm=Naklillm()
prompt="What is the capital of Nepal?"

# print(llm.generate_text(prompt))


