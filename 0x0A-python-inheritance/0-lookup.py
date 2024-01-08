#!/usr/bin/python3
"""The object attribute lookup function."""


def lookup(obj):
    """A list of an object's available attributes."""
    return (dir(obj))
