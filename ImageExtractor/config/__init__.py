import os
from dotenv import load_dotenv # type: ignore
from pydantic import BaseModel # type: ignore

load_dotenv()

class Setting(BaseModel):
    debug: bool = os.getenv("DEBUG")
    echo_active: bool = os.getenv("ECHO_ACTIVE")
