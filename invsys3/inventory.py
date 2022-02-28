from invSys3 import json_stuff


class Resource:
    def __init__(self, resource_array):
        name = resource_array[0]
        description = resource_array[1]
        amount = resource_array[2]


class Item:
    def __init__(self, item_array):
        name = item_array[0]
        description = item_array[1]


class Inventory:
    def __init__(self, path):
        item_list = []
        resource_list = []
        json_data = json_stuff.read_from_json_file(path)
        for item_array in json_data["items"]:
            item_list.append(Item(item_array))

        for resource_array in json_data["resources"]:
            resource_list.append(Resource(resource_array))


def create_inventory(base_path):
    file = open(base_path + "inv.json", "w")
    file.close()

    data = {
        "items": [],
        "resources": []
    }

    json_stuff.write_to_json_file(base_path + "inv.json", data)