from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
from importlib.machinery import SourceFileLoader, SourcelessFileLoader

def import_module(path: Path):
    name = path.stem
    return SourceFileLoader(name, str(path.resolve())).load_module()

def import_module3(path: Path):
    name = path.stem
    return SourcelessFileLoader(name, str(path.resolve())).load_module()

def import_module2(path: Path):
    name = path.stem
    spec = spec_from_file_location(name, str(path.resolve()))
    module = module_from_spec(spec)
    # spec.loader.exec_module(module)
    return spec, module

import_module(Path("/home/david/Bureau/projets/fastwork/module_test"))

path = Path("/home/david/Bureau/projets/fastwork/module_test")
