from pathlib import Path

import yaml

CONFIG = Path("config/notes.yaml")


def load_config():
    with open(CONFIG, "r") as f:
        return yaml.safe_load(f)
