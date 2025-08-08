from fastapi import FastAPI
from app.api import router

app = FastAPI(title="RAG Chatbot Backend")
app.include_router(router)
