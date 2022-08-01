#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    Instantiation with size: def __init__(self, size)::
    size validated by integer_validator and private
    the area() method must be implemented, prints the area of a square
    """
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        return (self.__size*self.__size)

    def __str__(self):
        return ('[Square] {}/{}'.format(self.__size, self.__size))
