def delete_keys(dictionary, *keys):
    for key in keys:
        if dictionary.get(key):
            del dictionary[key]
