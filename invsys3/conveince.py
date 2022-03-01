def get_user_data_path(author_id, file):
    path = "invSys3/Users/" + str(author_id) + "/" + file
    if not path.__contains__(".json"):
        path = path + ".json"
    return path
