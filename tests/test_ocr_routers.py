from fastapi.testclient import TestClient

from ImageExtractor.constants.path_constant import IMAGE_UPLOAD_DIR
from ImageExtractor.routers.ocr_routes import router

client = TestClient(router)


def test_get_available_models():
    response = client.get("/available-models/")
    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]
    assert response.json() == {"success": True, "models": []}


def test_process_image():
    test_image_dir = IMAGE_UPLOAD_DIR
    for img in test_image_dir.glob("*"):
        with open(img, "rb") as f:
            response = client.post("/process-image/", files={"image": (img.name, f)})
        filename = img.suffix
        assert filename in [".jpg", ".jpeg", ".png"]
        assert response.status_code == 200
