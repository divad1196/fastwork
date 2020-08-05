import json
import os
from pathlib import Path
from .validator import ConfigSchema
from ..defaults import CALL_PATH, DEFAULT_CONFIG_ENV_VAR, DEFAULT_CONFIG_NAME

def Config():
    LOCAL_CONFIG = Path(CALL_PATH).joinpath(DEFAULT_CONFIG_NAME)
    ENV_CONFIG_PATH = os.getenv(DEFAULT_CONFIG_ENV_VAR)

    config_path = LOCAL_CONFIG

    if not config_path.is_file() and ENV_CONFIG_PATH:
        config_path = Path(ENV_CONFIG_PATH).resolve()

    if config_path.is_file():
        with open(config_path, 'r') as f:
            config = json.load(f)
    else:
        config = {}
    config = ConfigSchema.validate(config).dict()

    if not config.get("base_path"):
        if config_path.is_file():
            config["base_path"] = config_path.resolve().parent
        else:
            config["base_path"] = CALL_PATH
    return config