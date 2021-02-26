import asyncio
from random import random

import aiohttp

async def hello(num, event):
    await event.wait()
    await asyncio.sleep(random())
    print(f"Hello from {num}")


async def unblock(event):
    sleep = asyncio.sleep(2)
    await sleep
    event.set()


async def hello_10():
    event = asyncio.Event()
    tasks = [hello(i, event) for i in range(10)]
    await asyncio.gather(*tasks, unblock(event))


asyncio.run(hello_10())
