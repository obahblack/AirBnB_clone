#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models

"""
Module BaseModel
Parent of all classes
"""


class BaseModel():
    """Base class for Airbnb clone project
    Methods:
       __init__(self, *args, **kwargs)
       __str__(self)
       __save(self)
       __repr__(self)
       to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes: random uuid, dates created/updated
        """
        if kwargs:
            for key, val in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetiime.strptime(kwargs["created_at"],
                                                         "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["update_at"],
                                                        "%Y-%m-dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return string representation of the BaseModel"""
        return ("[{}] ({}) {}".
                format(self.__class__.name__, self.id, self.__dict__))

    def __repr__(self):
        """
        Return string representation
        """
        return (self.__str__())

    def save(self):
        """
        Update instance with updated time and save
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dic with string formatts of times; add class info to dic
        """
        result = self.__dict__.copy()
        result['__class__'] = type(self).__name__
        result['created_at'] = result['created_at'].isoformat()
        result['updated_at'] = result['updated_at'].isoformat()
        return result

    @classmethod
    def from_dict(cls, dict_obj):
        # create a new instance of the class
        instance = cls()

        # set the attributes of the instance based on the dictionary
        for key, value in dict_obj.items():
            if key == "__class__":
                continue
            elif key == "created_at" or key == "updated_at":
                value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
            setattr(instance, key, value)

        return instance
