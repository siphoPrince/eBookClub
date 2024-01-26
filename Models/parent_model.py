#!/usr/bin/python3
"""Parent Model where all the class
will inherit from"""
from uuid import uuid4
from datetime import datetime


class Parentmodel:
    """parent model with the f.f attr
       id, created_at, updated_at
    """
    def __init__(self, *args, **kwargs):
    """initialize attr"""
    if not kwargs:
    self.id = str(uuid4())
    self.created_at = datetime.now()
    self.updated_at = datetime.now()
    else:
         if 'id' in kwargs:
                self.id = kwargs['id']
            else:
                self.id = str(uuid4())
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.created_at = datetime.now()
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.updated_at = datetime.now()

    def __str__(self):
        """String repr of the Parent Model Class"""
        return f"[{self.__class__.__name__}] {self.__dict__}"


