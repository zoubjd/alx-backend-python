#!/usr/bin/env python3
'''Add type annotations using TypeVar'''
import typing

T = typing.TypeVar('T')  # Define a TypeVar for the default value type


def safely_get_value(
    dct: typing.Mapping,
    key: typing.Any,
    default: typing.Union[T, None] = None
) -> typing.Union[typing.Any, T]:
    """Safely gets a value from a dictionary or returns a default value"""
    if key in dct:
        return dct[key]
    else:
        return default
