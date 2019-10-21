import base64
import time
from django.core.files.base import ContentFile


def millis():
    return int(round(time.time() * 1000))


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


def base64_to_file(data):
    format, imgstr = data.split(';base64,')
    ext = format.split('/')[-1]
    _name = f'{millis()}.{ext}'
    return _name, ContentFile(base64.b64decode(imgstr), name=_name)


def save_image_field(image_field, base64_str):
    if base64_str is not None:
        _name, _content = base64_to_file(base64_str)
        image_field.save(name=_name, content=_content)
