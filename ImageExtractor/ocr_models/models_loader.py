from easyocr import Reader as EasyOCRReader

from ..utility.logger import logger

# from paddleocr import PaddleOCR


# Store preloaded models
ocr_models = {}


def load_ocr_models():
    try:
        logger.info("Loading OCR models...")
        # ocr_models['tesseract'] =
        ocr_models["easy"] = EasyOCRReader(lang_list="en")
        # ocr_models['paddle'] = PaddleOCR()
        logger.info("✅ All OCR models loaded :) ")
    except Exception as e:
        logger.error(f"Error in load_ocr_models function: {e}")
        raise e


def get_ocr_model(name: str):
    return ocr_models.get(name)
