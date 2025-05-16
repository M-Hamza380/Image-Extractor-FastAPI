from pydantic import BaseModel, Field


class AvailableModels(BaseModel):
    """Response available models"""

    success: bool = Field(
        default_factory=bool, description="Message for display with true or false"
    )
    models: list = Field(default_factory=list, description="List of available models")
