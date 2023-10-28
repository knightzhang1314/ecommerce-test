from typing import Dict

import yaml


def read_yaml(fp: str) -> Dict:
    with open(fp, "r") as f:
        data = yaml.safe_load(f)
        return data
