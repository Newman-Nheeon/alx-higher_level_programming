#!/usr/bin/python3
def no_c(my_string):
    rev = ""
    for i in range(0, len(my_string)):
        if my_string[i] != 'c' and my_string != 'C':
            rev = rev + my_string[i]
    return rev
