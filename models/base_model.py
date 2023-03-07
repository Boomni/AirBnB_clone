#!/usr/bin/env python3
"""Module base_model"""
import uuid
import datetime


class BaseModel:
    """
    BaseModel defines all common attributes/methods for other classes
    """

    def __init__(self):
        """
        Public instance attributes:

        Args:
            id: string - assign with an uuid when an instance is created
            created_at: datetime - current datetime when an instance is created
            updated_at: datetime - current datetime when an instance is created
                        updated every time you change your object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """prints: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns dictionary containing
        all keys/values of __dict__ of the instance
        """
        result = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                value = value.isoformat()
            result[key] = value
        result['__class__'] = self.__class__.__name__
        return result
