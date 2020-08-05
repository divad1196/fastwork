from fastapi import FastAPI
app = FastAPI()

import uvicorn

from .modules import ModuleRegistry
from .models import DatabaseHandler
from .config import Config


class Framework:
    def __init__(self):
        config = Config()
        self.config = config
        self.app = FastAPI()
        self._create_db_mgr()
        self._create_modules_registry()

    def _init(self):
        self._init_modules_registry()
        self._init_db_mgr()

    def _create_db_mgr(self):
        database = self.config.get("database")
        self.db = DatabaseHandler(database)

    def _create_modules_registry(self):
        self.modules = ModuleRegistry()

    def _init_db_mgr(self):
        self.db.init()

    def _init_modules_registry(self):
        modules = self.config.get("modules", [])
        base_path = self.config.get("modules", [])
        self.modules.load_modules(modules)

    def run(self):
        self._init()
        server_params = self.config.get("server", {})
        uvicorn.run(self.app, **server_params)

framework = Framework()
