#!/usr/bin/python3
class Square:
    """
    Printing a square
    """
    def __init__(self, __size=0):
        self.__size = __size
        if type(__size) is not int:
            raise TypeError('size must be an integer')
        if __size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        return (self.__size*self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        for index in range(self.__size):
            if self.__size != 0:
                print('#'*self.__size)
