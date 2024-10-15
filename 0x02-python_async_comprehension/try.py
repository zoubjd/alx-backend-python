#!/usr/bin/env python3
import asyncio

async def async_generator():
    for i in range(5):
        await asyncio.sleep(1)
        yield i

# Using asynchronous comprehension to collect data:
async def main():
    result = [i async for i in async_generator()]
    print(result)

# Running the asynchronous code
asyncio.run(main())
