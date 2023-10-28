from abc import ABC


class BaseService(ABC):
    def run(self) -> None:
        raise NotImplementedError("Not implement the service.")
