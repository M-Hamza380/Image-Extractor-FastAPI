from functools import lru_cache

from ..config import Settings


@lru_cache
def get_setting():
    """Returns the application settings"""
    return Settings()
