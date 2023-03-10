#!/usr/bin/env python3
"""
Module base_model that implements the BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """
        Returns the string representation of BaseModel class
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing
        all keys/values of __dict__ of the instance

        - only instance attributes set will be returned
        - a key __class__ is added to dictionary with class name of the object
        - created_at and updated_at is converted to string object in ISO format
        """
        result = {**self.__dict__}
        if isinstance(result["created_at"], datetime):
            result["created_at"] = result["created_at"].isoformat()
        if isinstance(result["updated_at"], datetime):
            result["updated_at"] = result["updated_at"].isoformat()
        result['__class__'] = self.__class__.__name__
        return result

    @classmethod
    def all(cls):
        """
        Returns a list of all instances of the current class
        """
        obj_dict = storage.all()
        return [obj for obj in obj_dict.values() if isinstance(obj, cls)]
