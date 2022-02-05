import json


def set2d_arr(data):
    w, h = 3, 3

    matrix = [[0 for x in range(w)] for y in range(h)]

    def make_arr():
        for i in range(h):
            for i1 in range(w):
                matrix[i][i1] = 0

    make_arr()

    data["value4"] = matrix


def run():
    file_path = "jsonStuff/test1.json"
    with open(file_path) as file:
        json_variables = json.load(file)
    print(json_variables)
    json_variables["value1"] = "UWU"
    print("\n\n")

    print(json_variables)
    print("\n\n")

    print(json_variables["value1"])
    print("\n\n\n")

    for i in json_variables:
        print(i)
        print(json_variables[i])

    print("\n\n\n")
    print(json_variables["value2"][0])

    print("\n\n\n")
    print(json_variables["value4"])

    set2d_arr(json_variables)

    print("\n\n\n")
    print(json_variables["value4"])

    json_variables["value4"][2][2] = "10"
    json_variables["value4"][0][0] = "UwU"
    print("\n\n\n")
    print(json_variables["value4"])
    print(json_variables["value4"][2][2])

