#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns
    the number of characters written:

    Prototype: def write_file(filename="", text=""):
    Create the file if doesn’t exist and overwrite the content
    of the file if it already exists.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
