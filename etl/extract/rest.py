from typing import Any, AsyncGenerator

from aiohttp import ClientSession
from etl.extract.base import Extractor


class RestExtractor(Extractor):
    def __init__(self) -> None:
        pass

    async def __call__(self) -> AsyncGenerator[Any, Any]:
        pass
