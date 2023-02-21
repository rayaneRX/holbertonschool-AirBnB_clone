#!/usr/bin/python3
"""base model"""

import uuid
from datetime import datetime
import models


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
            models.storage.new(self)
        if type(self.created_at) is str:
            self.created_at = datetime.fromisoformat(self.created_at)
        if type(self.updated_at) is str:
            self.updated_at = datetime.fromisoformat(self.updated_at)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        new_dict = {}
        new_dict["__class__"] = f"{self.__class__.__name__}"
        for key, value in self.__dict__.items():
            if key == "updated_at":
                new_dict[key] = self.updated_at.isoformat()
            elif key == "created_at":
                new_dict[key] = self.created_at.isoformat()
            else:
                new_dict[key] = value
        return new_dict
