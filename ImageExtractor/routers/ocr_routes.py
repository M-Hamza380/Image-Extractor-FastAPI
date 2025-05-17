import os
import uuid
from pathlib import Path

import aiofiles
from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import FileResponse

from ..constants.path_constant import IMAGE_UPLOAD_DIR
from ..utility.logger import logger
from ..validation_schemas.response_schemas import AvailableModels

# Create router for instance
router = APIRouter()


@router.get("/available-models/", response_model=AvailableModels)
async def get_available_models() -> AvailableModels:
    """Get list of available models"""
    try:
        # models = ocr
        return AvailableModels(success=True)
    except Exception as e:
        logger.error(f"Error in get_available_models function: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/process-image/", response_class=FileResponse)
async def process_image(image: UploadFile = File(...)):
    """Process a single image with available models"""
    try:

        SUPPORTED_IMAGE_FORMATS = [".jpg", ".jpeg", ".png"]
        filename = image.filename or ""

        file_extension = os.path.splitext(filename)[1].lower()
        if file_extension not in SUPPORTED_IMAGE_FORMATS:
            logger.warning(f"Invalid file extension: {file_extension}")
            raise HTTPException(
                status_code=400,
                detail=f"Invalid file extention. Allowed/Supported formats: {', '.join(SUPPORTED_IMAGE_FORMATS)}",
            )

        upload_dir = Path(IMAGE_UPLOAD_DIR)
        if not os.path.exists(upload_dir):
            raise FileNotFoundError(f"File not found at that path: {upload_dir}")

        safe_filename = f"{filename}_{uuid.uuid4().hex[:4]}{file_extension}"
        file_path = upload_dir / safe_filename
        content = await image.read()

        async with aiofiles.open(file_path, mode="wb") as f:
            await f.write(content)

        logger.info("process_image route successfully compelete!")

        return FileResponse(
            str(file_path),
            media_type="application/octet-stream",
            filename=safe_filename,
        )

    except Exception as e:
        logger.error(f"Error in process-image router: {e}")
        raise HTTPException(status_code=500, detail=str(e))
