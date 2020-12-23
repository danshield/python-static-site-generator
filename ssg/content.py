import re
from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping):
    __delimiter = "^(?:-+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)
    @property
    def body(self):
        return self.data["content"]
    @property
    def type(self):
        return self.data["type"]

    @classmethod()
    def load(self, cls, string):
        _, fm, content = Content.__regex.split(string, 2)
        load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content


    def __getitem__(self, key):
        return self.data['key']

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {};
        for item in self.data.items():
           if not item.key == 'content':
               data[key] = item.value
        return str(data)







