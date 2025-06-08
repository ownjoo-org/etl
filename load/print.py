from typing import AsyncIterable

from src.app.etl.load.base import Loader


class PrintLoader(Loader):
    pass

    async def __call__(self, a_iter: AsyncIterable) -> None:
        async for each in a_iter:
            print(each)
