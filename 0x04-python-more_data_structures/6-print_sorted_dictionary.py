#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered = sorted(a_dictionary)
    for index in ordered:
        print('{}: {}'.format(index, a_dictionary[index]))
