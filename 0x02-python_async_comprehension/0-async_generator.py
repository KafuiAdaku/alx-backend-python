#!/usr/bin/env python3
"""
The coroutine will loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """Yields a random integer between 1 and 10"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
