from abc import ABC, abstractmethod
from typing import Any, AsyncIterator


class Loader(ABC):
    @abstractmethod
    def __call__(self, a_iter: AsyncIterator) -> Any:
        pass
