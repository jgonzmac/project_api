import json
import os
#__name__ = "__main__"
information = ('users-information.json')

def json_reader(jsonfilename):
    with open(jsonfilename, 'r') as py_dicc:
        json_read = json.load(py_dicc)
        return(json_read)

data_users = json_reader(information)
print(data_users)