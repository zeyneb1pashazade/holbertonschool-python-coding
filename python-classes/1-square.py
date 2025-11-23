#!/usr/bin/python3
"""
this module defines a class Square with input validation.
it demonstrates how to sanitize data during object instantiation.
"""


class Square:
    """
    represnts a square with strict input validation.

    attributes:
        __size (int): the size of the square (private).
    """

    def __init__(self, size=0):
        """
        initializes the square with type and value checks.

        args:
            size (int): the size of the square. defaults to 0.

        raizes:
            TypeError: if size is not an integer.
            ValueError: if size less than 0.
        """
        # 1st. Type validation: check if it`s an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # 2nd. Value validation: check if it`s non-negative
        if size < 0:
            raise ValueError("size must be >= 0")

        # 3rd. Safe storage: only if passed above, store privately
        self.__size = size
