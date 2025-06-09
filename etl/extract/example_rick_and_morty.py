from typing import Any, AsyncGenerator

from aiohttp import ClientSession
from etl.extract.rest import RestExtractor


class RickAndMortyExtractor(RestExtractor):
    async def __call__(self) -> AsyncGenerator[Any, Any]:
        async with ClientSession() as session:
            async with session.get('https://rickandmortyapi.com/api/character') as resp:
                data = await resp.json()
                async for item in data.get('results'):
                    yield item
