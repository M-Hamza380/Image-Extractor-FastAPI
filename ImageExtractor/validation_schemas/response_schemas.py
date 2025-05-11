from pydantic import BaseModel, Field # type: ignore
from typing import List, Dict, Optional, Any


class AvailableModels(BaseModel):
    """Response available models"""
    success: bool = Field(
        default_factory = bool,
        description = ''
    )
    models: list = Field(
        default_factory = list,
        description = 'List of all models'
    )
    
