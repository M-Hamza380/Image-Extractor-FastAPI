from contextlib import asynccontextmanager
from pathlib import Path

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from ImageExtractor.config import Settings
from ImageExtractor.constants.path_constant import STATIC_DIR
from ImageExtractor.ocr_models.models_loader import load_ocr_models
from ImageExtractor.routers.route import route
from ImageExtractor.utility.common import get_setting
from ImageExtractor.utility.logger import logger

# Add templating files directory for serving html pages
base_path = Path(__file__).parent
template_path = base_path / "templates"
templates = Jinja2Templates(directory=str(template_path))


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        load_ocr_models()
        yield
    except Exception as e:
        raise e


app = FastAPI(
    title="OCR API",
    description="Extract data from image, images or pdf file using multiple OCR models!",
    vresion="0.0.1",
    lifespan=lifespan,
)

# Configure CROS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add static files directory for serving staticfiles
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


# Include router
app.include_router(route)


# Health check endpoint
@app.get("/", response_class=HTMLResponse)
def index(request: Request, setting: Settings = Depends(get_setting)):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    try:
        setting = get_setting()
        logger.critical(
            f"Starting the server with Settings: {setting.debug}, type of: {type(setting)}"
        )
        if setting.debug:
            logger.debug("Debug mode is enabled")
            uvicorn.run("main:app", host="localhost", port=1253, reload=True)
        else:
            logger.debug("Debug mode is disable")
            uvicorn.run("main:app", host="localhost", port=1253, workers=2)
    except Exception as e:
        logger.error(f"Error in starting the server: {e}")
        raise HTTPException(status_code=500, detail=str(e))
