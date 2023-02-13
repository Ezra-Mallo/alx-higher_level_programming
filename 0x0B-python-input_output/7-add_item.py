#!/usr/bin/python3

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file =  __import__('6-load_from_json_file').load_from_json_file
filename= "add_item.json"
count = len(argv)
if __name__ == "__main__":
    try:
        read_content = load_from_json_file(filename)
        print(count)
    except FileNotFoundError:
        read_content = []

    if count > 1:
        argv_content = list(argv[1:])
        read_content.extend(argv_content)
        save_to_json_file(read_content, filename)
