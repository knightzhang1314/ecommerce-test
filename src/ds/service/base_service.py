from abc import ABC

from ds.schema.base_schema import BaseObject


class BaseService(ABC):
    def run(self) -> BaseObject:
        raise NotImplementedError("Not implement the service.")
