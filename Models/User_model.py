#!/usr/bin/python3
"""User model"""
from Models.parent_model import Parentmodel


class User(Parentmodel):
    """user class"""
    name = ""
    surname = ""
    email = ""
    password = ""
