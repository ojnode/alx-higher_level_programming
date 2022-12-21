#!/usr/bin/python3
# 0-square.py by Ojinnaka Prince
"""A module that defines a square """


class Square:
    """Class defined for square generation.

    Args:
        size (int): length of one side of square

    Attributes:
        __size (int): length of one side of square

    Raises:
    TypeError: if size is not an integer
    ValueError: if size is less than 0

    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be integer')
        if size < 0:
            raise ValueError('size must be >=0')
        self.__size = size

    def area(self):
        """Caulates area of square.

        Attributes:
        __size (int): length of one side of square

        Returns:
            area (int): length of one side, squared

        """
        area = self.__size * self.__size
        return area
