#!/usr/bin/env python3
"""asyncio basics"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """returns a float"""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
