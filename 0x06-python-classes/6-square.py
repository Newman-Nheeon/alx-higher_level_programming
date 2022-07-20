#!/usr/bin/python3
class Square:
    """
    Printing a square
    """
    def __init__(self, __size=0, position=(0, 0)):
        self.__size = __size
        self.position = position
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) is not 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for index in range(self.__position[1]):
                print()
            for index in range(self.__size):
                print('{}{}'.format(' '*self.position[0], '#'*self.__size))
