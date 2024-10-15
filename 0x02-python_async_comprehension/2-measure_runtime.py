#!/usr/bin/env python3
"""async tha bi"""
import asyncio
import typing
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """mesuring time"""
    startTime = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    return time.perf_counter() - startTime
