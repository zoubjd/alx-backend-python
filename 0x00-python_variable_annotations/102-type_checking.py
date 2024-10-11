#!/usr/bin/env python3
"""mypy"""
import typing
Tuple = typing.Tuple


def zoom_array(
        lst: typing.List[typing.Any],
        factor: typing.Any = 2) -> typing.List[int]:
    zoomed_in: typing.List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
