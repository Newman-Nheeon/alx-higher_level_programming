#!/usr/bin/python3
def no_c(my_string):
    rev = ""
    for i in my_string(0, len(my_string)):
        if my_string[i] == "c" or "C":
            rev = rev + my_string[i]
    return rev
