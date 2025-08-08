from fastapi import APIRouter
from app.models.schema import ChatRequest, ChatResponse
from app.services.llm_service import ask_llm
from app.services.vector_store_service import search_similar_vectors
import numpy as np

router = APIRouter()

def mock_embedding(text: str):
    return np.random.rand(384).tolist()

@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    user_msg = req.message
    query_vector = mock_embedding(user_msg)
    context_chunks = search_similar_vectors(query_vector)
    context = "\n".join(context_chunks) or "No relevant data found."
    answer = await ask_llm(context, user_msg)
    return ChatResponse(answer=answer)
