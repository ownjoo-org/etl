from abc import ABC, abstractmethod
from typing import Any, AsyncIterable, Generator


class Transformer(ABC):
    pass

    @abstractmethod
    async def __call__(self, a_iter: AsyncIterable) -> Generator[Any, Any, Any]:
        pass
