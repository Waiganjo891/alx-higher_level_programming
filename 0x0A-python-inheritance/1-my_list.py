#!/usr/bin/python3
"""An inherited list."""


class MyList(list):
    """It prints for the built-in list class."""

    def print_sorted(self):
        """A sorted ascending order."""
        print(sorted(self))
