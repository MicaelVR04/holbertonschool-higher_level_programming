#!/usr/bin/python3
"""
This module defines a Square class that validates its size
and provides a method to compute the area of the square.
"""


class Square:
    """
    This class represents a square and controls access to its size
    to ensure it is always a valid non-negative integer.
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance with a given size.

        Args:
            size (int): The length of one side of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Return the area of the square based on its current size.
        """
        return self.__size * self.__size
