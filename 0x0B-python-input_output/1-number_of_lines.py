#!/usr/bin/python3
def number_of_lines(filename=""):
    """
    Returns the number of lines of a text file
    """
    with open(filename) as f:
        return len(f.readlines())
