from typing import AsyncIterable

from load.base import Loader


class PrintLoader(Loader):
    pass

    async def __call__(self, a_iter: AsyncIterable) -> None:
        async for each in a_iter:
            print(each)
