from pprint import pprint
import os

file_list = os.listdir()
def new_file(file_list):
    dict_i = {}
    for file in file_list:
        if file.endswith('.txt'):
            counter = 0
            with open(file, encoding='utf-8') as f:
                data = f.readlines()
                for a in data:
                    counter += 1
                    dict_i[file] = (counter, data)
    for i in sorted(dict_i.items(), key=lambda x: x[1]):
        pprint(i)

new_file(file_list)
