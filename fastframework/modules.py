from importlib import import_module, reload
from importlib.machinery import SourceFileLoader
import types
from pathlib import Path
from typing import List, Union, Optional
from .defaults import CALL_PATH

PathType = Union[Path, str]
DEFAULT_BASE_PATH = CALL_PATH

def _absolute_path_import(path: Path, name: str):
    loader = SourceFileLoader(name, str(path.resolve()))
    module = types.ModuleType(loader.name)
    loader.exec_module(module)
    return module

def absolute_path_import(path: Path, name=None):
    path = Path(path)
    name = name or path.stem
    if path.is_file():
        return _absolute_path_import(path.resolve(), name)
    if path.is_dir():
        init_file = path.joinpath("__init__.py")
        if init_file.is_file():
            return _absolute_path_import(init_file.resolve(), name)
    return

class ModuleRegistry:

    def __init__(self, base_path: PathType = DEFAULT_BASE_PATH):
        self._base_path = Path(base_path).resolve()
        self._registry = {}

    def import_module(self, path: Path):
        return absolute_path_import(path)

    def _load_module(self, module: PathType, base_path: PathType):
        module_path = Path(base_path).joinpath(module).resolve()
        name = module_path.stem
        print("Loading module at '{path}'".format(path=module_path))
        module = self.import_module(module_path)
        self._registry[name] = {
            "module": module,
            "path": module_path,
        }

    def load_modules(self, modules: List[PathType], base_path: Optional[PathType] = None):
        if base_path is None:
            base_path = self._base_path
        for m in modules:
            self._load_module(m, base_path)

    # def reload(self):
    #     for

    def __getitem__(self, module):
        return self._registry[module]["module"]

    def __iter__(self):
        return iter(self._registry)

    def items(self):
        return {
            key: value["module"]
            for key, value in self._registry.items()
        }.items()
        # return {
        #     key: self[key]
        #     for key in self
        # }.items()

    def module_objects(self):
        return [m["module"] for m in self._registry.values()]

    def module_path(self, module):
        return self._registry[module]["path"]