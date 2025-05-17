from pathlib import Path


def ensure_make_dir(path: Path) -> Path:
    """Create directory if it doesn't exist and return path"""
    path.mkdir(parents=True, exist_ok=True)
    return path


# Add directories to the path
BASE_DIR = Path(__file__).parent.parent.parent
STATIC_DIR = BASE_DIR / "static"
IMAGES_DIR = STATIC_DIR / "images"

IMAGE_UPLOAD_DIR = ensure_make_dir(IMAGES_DIR / "uploads")
IMAGE_OUTPUT_DIR = ensure_make_dir(IMAGES_DIR / "outputs")
