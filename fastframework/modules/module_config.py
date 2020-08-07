from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path

class ModuleConfigSchema(BaseModel):
    name: str
    depends: List[str] = []

