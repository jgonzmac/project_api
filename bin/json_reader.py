import json
import os

def json_reader(jsonfilename):
    file_path = os.path.abspath(__file__).replace('bin', 'data').replace('json_reader.py', jsonfilename)
    with open(file_path, 'r', encoding='utf-8') as py_dicc:
        json_read = json.load(py_dicc)
        return(json_read)


def json_write(data: list, jsonfilename: str):
    pass


def json_delete():
    pass