from abc import ABC

from ds.schema.base_schema import BaseObject


class BaseLoader(ABC):
    def load(self) -> BaseObject:
        raise NotImplementedError("Not implement.")
