
import ast
import os

def append_to_txt(path,content):
    with open(path, 'a') as f:
        f.write(content)


def read_from_txt(path):
    messages = []
    with open(path,'rw') as f:
        for line in f.readlines():
            messages.append(ast.literal_eval(line.strip("\n")))
    return messages

