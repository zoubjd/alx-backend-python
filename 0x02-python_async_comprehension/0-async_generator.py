#!/usr/bin/env python3
"""async"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, any, any]:
    """yield"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
