from fastapi import FastAPI
from pydantic import BaseModel
from retriever import Retriever
from llm import generate_answer

app = FastAPI()
retriever = Retriever()

class ChatRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "MiniGPT backend is alive 🚀"}

@app.post("/chat")
def chat(req: ChatRequest):
    docs = retriever.retrieve(req.question, top_k=6)

    if not docs:
        return {
            "answer": "I don't know.",
            "context": []
        }

    context = "\n\n".join(docs)

    answer = generate_answer(context, req.question)

    return {
        "answer": answer,
        "context": docs
    }
