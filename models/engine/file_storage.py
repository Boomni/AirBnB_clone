#!/usr/bin/python3
"""
Module file_storage.py that defines the FileStorage class
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage class serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    cls = key.split(".")[0]
                    obj = eval(cls)(**value)
                    FileStorage.__objects[key] = obj
        except (IOError, json.JSONDecodeError) as e:
            pass
