from typing import Any, AsyncIterable, Generator

from etl.transform.base import Transformer


class PassThroughTransformer(Transformer):
    pass

    async def __call__(self, a_iter: AsyncIterable) -> Generator[Any, Any, Any]:
        async for each in a_iter:
            yield each
