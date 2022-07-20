#!/usr/bin/python3
class Square:
    """
    Add in the class a private instance attribute, instantiation and
    conditions to raise errors in the execution of the code
    """
    def __init__(self, __size=0):
        self.__size = __size
        if type(__size) is not int:
            raise TypeError('size must be an integer')
        if __size < 0:
            raise ValueError('size must be >= 0')
