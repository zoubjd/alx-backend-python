#!/usr/bin/env python3
"""python annotations"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]
                   ) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """returns a tuple"""
    return [(i, len(i)) for i in lst]
