#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = my_list
    if idx >= 0 and idx < len(newlist):
        newlist[idx] = element
    return newlist


list1 = [1, 2, 3, 4, 5]
new_in_list(list1, 3, 5)
