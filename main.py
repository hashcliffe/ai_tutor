from fastapi import FastAPI, Request
from pydantic import BaseModel
from agents.tutor_agent import TutorAgent

app = FastAPI()
tutor_agent = TutorAgent()

# Define the request body format
class Query(BaseModel):
    question: str

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Tutor!"}

# /ask endpoint to send questions
@app.post("/ask")
def ask_question(query: Query):
    response = tutor_agent.handle_query(query.question)
    return {"response": response}
