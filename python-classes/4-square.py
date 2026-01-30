#!/usr/bin/python3
"""
This module defines a Square class that manages a private size attribute
using property getters and setters with proper validation.
"""


class Square:
    """
    This class represents a square and provides controlled access
    to its size while allowing area computation.
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance with an optional size.

        Args:
            size (int): The length of one side of the square.
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
        Set the size of the square after validating its type and value.

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
        Return the area of the square based on its size.
        """
        return self.__size * self.__size
