import json


def write_to_json_file(path, file_name, data):
    file_path_name_w_ext = '' + path + '' + file_name + '.json'
    with open(file_path_name_w_ext, 'w') as fp:
        json.dump(data, fp)


def run():
    json_data = {
        "value1": "one",
        "value2": ["string", 1, True],
        "value3": 3,
        "value4": "2d array here"
    }

    write_to_json_file("jsonStuff/", "test1", json_data)


