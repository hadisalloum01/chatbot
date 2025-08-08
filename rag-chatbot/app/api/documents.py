from fastapi import APIRouter, UploadFile, File
from app.services.vector_store_service import add_to_vector_store
import numpy as np

router = APIRouter()

def mock_embedding(text: str):
    return np.random.rand(384).tolist()

@router.post("/documents/upload")
async def upload(file: UploadFile = File(...)):
    content = (await file.read()).decode("utf-8")
    embedding = mock_embedding(content)
    add_to_vector_store(content, embedding)
    return {"status": "uploaded"}
