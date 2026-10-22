from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def landing_page():

    return {"message": "Welcome to the Multi-AI Chatbot API"}

@app.get("/health")
def health():

    return{
        "status":"ok"
    }