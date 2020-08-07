from importlib import reload
from pathlib import Path
from typing import List, Union, Optional
from ..defaults import CALL_PATH
from .tools import absolute_path_import, get_module_readme_description, get_module_config

PathType = Union[Path, str]
DEFAULT_BASE_PATH = CALL_PATH


class ModuleRegistry:
    def __init__(self, base_path: PathType = DEFAULT_BASE_PATH):
        self._base_path = Path(base_path).resolve()
        self._registry = {}
        self._modules = {}
        self._search_dir = []

    def _get_path(self, path, base_path: Optional[PathType] = None):
        if base_path is None:
            base_path = self._base_path
        return Path(base_path).joinpath(path).resolve()

    def _get_module_description(self, path: Path):
        return get_module_readme_description(path)

    def _get_module_config(self, path: Path):
        return get_module_config(path)

    def register_search_dir(self, dir: PathType, base_path: Optional[PathType] = None):
        path = self._get_path(dir, base_path)
        if path not in self._search_dir:
            self._search_dir.append(path)
        for module in path.iterdir():
            self.register_module(module.resolve())

    def register_module(self, module: PathType, base_path: Optional[PathType] = None):
        if base_path is None:
            base_path = self._base_path
        module_path = Path(base_path).joinpath(module).resolve()
        name = module_path.stem
        description = self._get_module_description(module_path)
        config = self._get_module_config(module_path)
        self._modules[name] = {
            "path": module_path,
            "description": description,
            "config": config,
        }
        return name
    
    def _find_module(self, name: str):
        for d in self._search_dir:
            for module in d.iterdir():
                if module.name == name:
                    return module.resolve()
        return None

    def imports(self, module: str):
        m = self.get(module)
        if m is not None:
            return m
        path = self._find_module(m)
        return self.import_module(path)

    def import_all(self):
        for module in self._modules:
            self.import_module(module)

    def import_module(self, path: Path, base_path: Optional[PathType] = None):
        path = self._get_path(path, base_path)
        name = self.register_module(path)
        module = self.load(name)
        return module

    def import_modules(self, paths: List[PathType], base_path: Optional[PathType] = None):
        for p in paths:
            self.import_module(p, base_path)

    def _load(self, path: Path):
        return absolute_path_import(path)

    def load(self, name: str):
        path = self._modules[name]["path"]
        print("Loading module {name} at '{path}'".format(
            name=name,
            path=path,
        ))
        module = self._load(path)
        self._registry[name] = module
        return module

    def load_modules(self, modules: List[str]):
        for m in modules:
            self.load(m)

    def module_objects(self):
        return [m["module"] for m in self._registry.values()]

    def path(self, module):
        """
            Get registered module's absolute path
        """
        return self._registry[module]["path"]

    def description(self, module: str):
        """
            Get registered module's description
        """
        return self._modules[module]["description"]

    def get(self, module: str, default=None):
        return self._registry.get(module, default)

    def __getitem__(self, module: str):
        return self._registry[module]

    def __iter__(self):
        return iter(self._registry)

    def items(self):
        return self._registry.items()

    def keys(self):
        return self._registry.keys()

    def values(self):
        return self._registry.values()