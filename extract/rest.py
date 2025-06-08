from typing import Any, AsyncGenerator

from aiohttp import ClientSession

from extract.base import Extractor


class RestExtractor(Extractor):
    pass

    async def __call__(self) -> AsyncGenerator[Any, Any]:
        async with ClientSession() as session:
            async with session.get('https://rickandmortyapi.com/api/character') as resp:
                data = await resp.json()
                for item in data.get('results'):
                    yield item
