from importlib.machinery import SourceFileLoader
import types
from pathlib import Path
from markdown import markdown
from ..defaults import DEFAULT_MODULE_CONFIG_FILENAME
from .module_config import ModuleConfigSchema

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

def get_module_readme_description(path: Path):
    path = Path(path).resolve()
    if path.is_dir():
        for f in path.iterdir():
            if f.name.lower() == "readme.md" and f.is_file():
                with open(f) as readme:
                    return markdown(readme.read())
    return ""

def get_module_config(path: Path):
    path = Path(path).resolve()
    config = {}
    if path.is_dir():
        config_file = path.joinpath(DEFAULT_MODULE_CONFIG_FILENAME)
        name = path.stem
        if config_file.is_file():
            with open(config_file, 'r') as f:
                config = json.load(f)
    if 'name' not in config:
        config['name'] = path.stem
    return ModuleConfigSchema.validate(config).dict()
