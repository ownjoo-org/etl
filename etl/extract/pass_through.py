from typing import Any, AsyncGenerator

from etl.extract.base import Extractor


class PassThroughExtractor(Extractor):
    async def __call__(self) -> AsyncGenerator[Any, Any]:
        for item in []:
            yield item
