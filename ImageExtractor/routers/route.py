from fastapi import APIRouter

from .ocr_routes import router as image_router

route = APIRouter()

route.include_router(image_router, prefix="/api/v1", tags=["Image Extractor"])
