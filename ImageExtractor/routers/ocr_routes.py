from fastapi import (
    APIRouter,
    File,
    UploadFile,
    Depends,
    Request,
    Form,
    HTTPException
)
import aiofiles
from pathlib import Path

from ..utility.logger import logger
from ..validation_schemas.response_schemas import AvailableModels

# Create router for instance
router = APIRouter()

@router.get("/available-models", response_model = AvailableModels)
async def get_available_models() -> AvailableModels:
    """Get list of available models"""
    try:
        models = ocr
        return AvailableModels(
            success = True,
            models = models
        )
    except Exception as e:
        logger.error(f"Error in get_available_models function: {e}")
        raise HTTPException(status_code = 500, detail=str(e))
    


