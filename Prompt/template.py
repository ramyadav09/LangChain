from langchain_core.prompts import PromptTemplate

# Simple dynamic prompt template
prompt = PromptTemplate(
    input_variables=["topic", "level", "question"],
    template="""
Explain the topic: {topic}

Difficulty Level:
{level}

Question:
{question}
""",
)
prompt.save("template.json")
# # Example usage
# result = prompt.format(
#     topic="Python",
#     level="Beginner",
#     question="What is a list in Python?"
# )

# print(result)
