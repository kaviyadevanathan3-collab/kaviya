from fastapi import FastAPI
from app.routes import file

app = FastAPI()

@app.get("/")
def landing_page():

    return {"message": "Welcome to the Multi-AI Chatbot API"}

@app.get("/health")
def health():

    return{
        "status":"ok"
    }

app.include_router(file.router)