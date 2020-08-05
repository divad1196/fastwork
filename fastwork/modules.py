from importlib import import_module, reload
from importlib.machinery import SourceFileLoader
from pathlib import Path
from typing import List, Union, Optional
from .defaults import CALL_PATH

PathType = Union[Path, str]
DEFAULT_BASE_PATH = CALL_PATH

class ModuleRegistry:

    def __init__(self, base_path: PathType = DEFAULT_BASE_PATH):
        self._base_path = Path(base_path).resolve()
        self._registry = {}

    def import_module(self, path: Path):
        if not path.is_dir():
            return
        init_file = path.joinpath("__init__.py")
        if not init_file.is_file():
            return
        name = path.stem
        return SourceFileLoader(name, str(init_file.resolve())).load_module()

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