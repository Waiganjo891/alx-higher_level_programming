#!/usr/bin/python3
"""Inherits a class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class"""
    if isinstance(obj, a_class):
        return True
    return False
