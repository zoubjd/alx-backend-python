#!/usr/bin/env python3
"""deals with str and int/float"""
import typing


def to_kv(k: str,
          v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """returns a tuple"""
    return (k, v ** 2)
