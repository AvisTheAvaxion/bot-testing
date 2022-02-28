import json


def write_to_json_file(path, data):
    file_path_name_w_ext = path
    with open(file_path_name_w_ext, 'w') as fp:
        json.dump(data, fp)


def read_from_json_file(path):
    with open(path) as file:
        data = json.load(file)
        return data


