#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """
    Reads n lines of a text file (UTF8) and prints it to stdout
    Prototype: def read_lines(filename="", nb_lines=0):
    Read the entire file if nb_lines is lower or equal to 0
    OR greater or equal to the total number of lines of the file
    """
    with open(filename) as f:
        text = f.readlines()
        if nb_lines <= 0 or nb_lines >= len(text):
            for i in text:
                print(i, end='')
        else:
            for i in range(nb_lines):
                print(text[i], end='')
