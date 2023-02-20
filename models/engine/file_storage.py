#!/usr/bin/python3
"""Store an object"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] \
            = obj.to_dict()

    def save(self):
        with open(FileStorage.__file_path, "w") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as file:
                dict = json.load(file)
                for key, value in jsonData.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
        except Exception:
            pass
