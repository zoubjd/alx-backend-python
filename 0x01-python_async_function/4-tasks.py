#!/usr/bin/env python3
"""async"""
import random
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """asyncs maxdelay n times"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    to_order = []
    for delay in delays:
        to_order.append(delay)
    for i in range(len(to_order)-1):
        for j in range(len(to_order)-1):
            if to_order[j] > to_order[j+1]:
                tmp = to_order[j]
                to_order[j] = to_order[j+1]
                to_order[j+1] = tmp
    return to_order
