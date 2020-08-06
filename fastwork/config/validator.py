from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path

class ServerConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 5000
    log_level: str = "info"

class WebConfig(BaseModel):
    cors: List[str] = []

class ConfigSchema(BaseModel):
    database: str = "sqlite:///fastwork.db"
    web: WebConfig = WebConfig()  # Possible because WebConfig is default constructible
    server: ServerConfig = ServerConfig()
    modules: List[Path] = []
    base_path: Optional[Path]

