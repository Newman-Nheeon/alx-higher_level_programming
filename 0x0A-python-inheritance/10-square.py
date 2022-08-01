#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    Instantiation with size validated by integer_validator and private
    the area() method must be implemented
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator('size', size)
        super().__init__(self.__size, self.__size)

    def area(self):
        return (self.__size*self.__size)
