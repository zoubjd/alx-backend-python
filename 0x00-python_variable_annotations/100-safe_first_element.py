#!/usr/bin/env python3
'''duck type annotations'''
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]
                       ) -> typing.Union[typing.Any, type(None)]:
    """Returns the first element if the list is not empty, otherwise None"""
    if lst:
        return lst[0]
    else:
        return None
