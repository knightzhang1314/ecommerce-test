from pathlib import Path
from typing import Dict

import yaml

from ds.core.model import ConfigModel


class Platform:
    """Base class for platform."""

    def __init__(self, scope: str = None) -> None:
        self._scope = scope

    @property
    def configs(self) -> ConfigModel:
        config_name = "config.yml"
        proj_path = Path(__file__).resolve().parent.parent
        root_path = proj_path.parent.parent
        config_path = proj_path.joinpath("configs")
        config = config_path.joinpath(config_name)
        source_config = self._read_yaml(str(config))
        source_config["root_path"] = root_path
        scope_config = {}
        if self._scope:
            scope_config_name = f"config-{self._scope}.yml"
            config = config_path.joinpath(scope_config_name)
            scope_config = self._read_yaml(str(config))
        return ConfigModel(**source_config, **scope_config)

    def _read_yaml(self, fp: str) -> Dict:
        with open(fp, "r") as f:
            data = yaml.safe_load(f)
            return data
