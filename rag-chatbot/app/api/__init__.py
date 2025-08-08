from fastapi import APIRouter
from .chat import router as chat_router
from .documents import router as doc_router

router = APIRouter()
router.include_router(chat_router)
router.include_router(doc_router)
