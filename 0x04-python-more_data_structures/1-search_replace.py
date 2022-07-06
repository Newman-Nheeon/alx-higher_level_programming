#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for index in my_list:
        if index != search:
            new_list[len(new_list):] = [index]
        else:
            new_list[len(new_list):] = [replace]
    return new_list
