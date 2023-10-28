from abc import ABC


class BaseWriter(ABC):
    def write(self) -> None:
        raise NotImplementedError("Not implement the writer.")
