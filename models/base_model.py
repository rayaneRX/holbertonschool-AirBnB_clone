#!/usr/bin/python3
"""base model"""

import uuid
from datetime import datetime


class BaseModel:
    """Class defining all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            # for key, value in kwargs.items():
            #     setattr(self, key, value)
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict = self.__dict__
        dict["__class__"] = f"{self.__class__.__name__}"
        dict["updated_at"] = self.updated_at.isoformat()
        dict["created_at"] = self.created_at.isoformat()
        return dict
