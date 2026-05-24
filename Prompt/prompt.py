from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

prompt_template = PromptTemplate(
    input_variables=["topic", "level", "question"],
    template="Explain the topic: {topic}\n\nDifficulty Level: {level}\n\nQuestion: {question}",
)

class PromptRequest(BaseModel):
    topic: str
    level: str
    question: str

@app.post("/")
def promptResult(body: PromptRequest):
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    prompt = prompt_template.format(
        topic=body.topic,
        level=body.level,
        question=body.question,
    )
    result = model.invoke(prompt)
    return {"summary": result.content}
