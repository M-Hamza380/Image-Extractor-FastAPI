from fastapi import FastAPI, Request # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from fastapi.templating import Jinja2Templates # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore
from pathlib import Path
import uvicorn # type: ignore

from ImageExtractor.config import Setting
from ImageExtractor.routers import ocr_routes
from ImageExtractor.utils.logger import logger

# Add templating files directory for serving html pages
base_path = Path(__file__).parent
template_path = base_path / "templates"
templates = Jinja2Templates(directory=template_path)

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
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    setting = Setting()

    if setting.debug:
        uvicorn.run('main:app', host='localhost', port='1253', reload=True)
    else:
        uvicorn.run('main:app', host='localhost', port='1253', workers=2)

