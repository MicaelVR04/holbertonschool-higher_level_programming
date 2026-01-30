#!/usr/bin/python3
"""
This module defines a Square class that supports size validation,
area calculation, and printing the square using the # character.
"""


class Square:
    """
    This class represents a square with a private size attribute
    and provides methods to compute area and print the square.
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance with an optional size.

        Args:
            size (int): The size of one side of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square after validating its value.

        Args:
            value (int): The new size of the square.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using the # character.
        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
