#!/usr/bin/python3
import sys

save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file


""" Adds all arguments to a Python list, and then save them to a file """
try:
    list = load("add_item.json")
except Exception:
    list = []

for i in sys.argv[1:]:
        list.append(i)

save(list, "add_item.json")
