#!/usr/bin/python3
"""
Module of a Square Class
"""


class Square:
    """Blueprint of a class square"""

    def __init__(self, size=0):
        """Initializes a new square.
        Args:
            size (int): The size of the new square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of a square
        Returns:
            Area of the square
        """
        return (self.__size * self.__size)
