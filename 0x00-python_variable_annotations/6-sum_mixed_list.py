#!/usr/bin/env python3
"""sums a mixed list"""
import typing


def sum_mixed_list(mixed_list: typing.List[typing.Union[int, float]]) -> float:
    """sum a mixed list"""
    return sum(mixed_list)
