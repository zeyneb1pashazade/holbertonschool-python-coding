#!/usr/bin/python3
"""
this module defines a class Square
"""


class Square:
    """
    it represents a square shape
    attributes:
        __size (int): the size of the square (private).
    """
    def __init__(self, size):
        """
        initializes a new Square instance.

        args:
            size (any): the size of the square. No validation is done yet.
        """
        # Assigning the incoming 'size' to the private attribute '__size'
        # the double underscore (__) tells python: "keep this hidden!"
        self.__size = size
