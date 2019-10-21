import json


class Jsonbody(object):

    def __init__(self, jsonText, encoding='utf-8'):
        data = json.loads(jsonText, encoding=encoding)
        for key, value in data.items():
            self.__dict__[key] = value
        self.json = data

    def __getattribute__(self, item):
        try:
            return super(Jsonbody, self).__getattribute__(item)
        except AttributeError:
            return None
