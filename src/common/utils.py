def delete_keys(dictionary, *keys):
    for key in keys:
        if dictionary.get(key):
            del dictionary[key]


def build_query_param(request, **kwargs):
    params = request.query_params
    queries = {}
    for key, value in kwargs.items():
        item = params.get(key)
        if item is not None:
            queries[value] = item
    return queries
