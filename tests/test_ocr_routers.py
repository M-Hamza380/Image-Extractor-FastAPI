from fastapi.testclient import TestClient

from ImageExtractor.routers.ocr_routes import router

client = TestClient(router)


def test_get_available_models():
    response = client.get("/available-models/")
    assert response.status_code == 200
