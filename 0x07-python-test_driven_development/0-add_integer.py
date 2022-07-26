#!/usr/bin/python3
"""
add_integer function

This function add two integers. Return an integer
"""


def add_integer(a, b=98):
    """
    Check if the parameters are float, if so, casted it to integer.
    If parameters are integer or float), raise an exception with a message. """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
