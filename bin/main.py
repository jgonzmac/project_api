from json_reader import json_reader
from methods import Methods


def parsing_params():
    pass


def main():
    methods = Methods()
    method_type: str = "post"
    data_base: str = "team.json"

    data_dict: dict = json_reader(data_base)

    if method_type == "post":
        methods.post(data_base=data_dict)
    


if __name__ == '__main__':
    main()