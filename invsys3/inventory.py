from invSys3 import json_stuff


class Resource:
    def __init__(self, resource_array):
        self.name = resource_array[0]
        self.description = resource_array[1]
        self.amount = resource_array[2]

    def to_array(self):
        this_resource = [self.name, self.description, self.amount]
        return this_resource


class Item:
    def __init__(self, item_array):
        self.name = item_array[0]
        self.description = item_array[1]

    def to_array(self):
        this_item = [self.name, self.description]
        return this_item


class Inventory:
    def __init__(self, path):
        self.item_list = []
        self.resource_list = []
        self.path = path

        json_data = json_stuff.read_from_json_file(path)

        for item_array in json_data["items"]:
            self.item_list.append(Item(item_array))

        for resource_array in json_data["resources"]:
            self.resource_list.append(Resource(resource_array))

    def add_resource(self, name, description, amount):
        new_resource = Resource([name, description, amount])
        has_resource = False

        for resource in self.resource_list:
            if resource.name == new_resource.name:
                resource.amount = int(resource.amount) + int(new_resource.amount)
                has_resource = True

        if not has_resource:
            self.resource_list.append(new_resource)

        self.save()

    def save(self):
        resources = []
        items = []

        for r in self.resource_list:
            resources.append(r.to_array())

        for i in self.item_list:
            items.append(i.to_array())

        data = {
            "resources": resources,
            "items": items
        }

        json_stuff.write_to_json_file(self.path, data)


def create_inventory(path):
    file = open(path, "w")
    file.close()

    data = {
        "items": [],
        "resources": []
    }

    json_stuff.write_to_json_file(path, data)