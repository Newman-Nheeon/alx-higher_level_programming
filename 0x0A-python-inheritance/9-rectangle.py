#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry
    Instantiation with width and height: def __init__(self, width, height):
    width and height are validated by integer_validator and private.
    the area() method must be implemented, print the area of a Rectangle
    """
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        return (self.__width*self.__height)

    def __str__(self):
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))
