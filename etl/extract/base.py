from abc import ABC, abstractmethod
from typing import Any, AsyncGenerator


class Extractor(ABC):
    pass

    @abstractmethod
    async def __call__(self) -> AsyncGenerator[Any, Any]:
        pass
