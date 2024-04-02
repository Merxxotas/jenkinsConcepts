import json


def read_names():
    json_file = open("names.json", "r")
    data: list = json.load(json_file)
    json_file.close()
    return data
