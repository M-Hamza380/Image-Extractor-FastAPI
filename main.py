from fastapi import FastAPI, Request, HTTPException # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from fastapi.templating import Jinja2Templates # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore
from fastapi.responses import HTMLResponse # type: ignore
from pathlib import Path
import uvicorn # type: ignore

from ImageExtractor.config import Setting
from ImageExtractor.routers import ocr_routes
from ImageExtractor.utils.logger import logger

# Add templating files directory for serving html pages
base_path = Path(__file__).parent
template_path = base_path / "templates"
templates = Jinja2Templates(directory=str(template_path))

app = FastAPI(
    title = "OCR API",
    description = "Extract data from image, images or pdf file using multiple OCR models!",
    vresion="0.0.1"
)

# Configure CROS
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# Add static files directory for serving staticfiles
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include router
app.include_router(ocr_routes, prefix="/api/v1", tags=['Image Extractor'])

# Health check endpoint
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    try:
        setting = Setting()
        logger.critical(f"Starting the server with Settings: {setting.debug}")
        if setting.debug:
            logger.debug('Debug mode is enabled')
            uvicorn.run('main:app', host='localhost', port='1253', reload=True)
        else:
            logger.debug('Debug mode is disable')
            uvicorn.run('main:app', host='localhost', port='1253', workers=2)
    except Exception as e:
        logger.error(f"Error in starting the server: {e}")
        raise HTTPException(status_code = 500, detail=str(e))

