from typing import AsyncIterable, Any, AsyncGenerator

from src.app.etl.load.base import Loader


class PassThroughLoader(Loader):
    pass

    async def __call__(self, a_iter: AsyncIterable) -> AsyncGenerator[Any, Any]:
        async for each in a_iter:
            yield each
