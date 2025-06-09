from typing import AsyncIterable

from etl.load.base import Loader


class PrintLoader(Loader):
    async def __call__(self, a_iter: AsyncIterable) -> None:
        async for each in a_iter:
            print(each)
