#!/usr/bin/pyhton3
"""Books Model"""
from Models.parent_model import Parentmodel


class Books(Parentmodel):
    title = ""
    Author = ""
    Catergory_name = ""
    catergory_number = 0
    Book_description = ""
    ref_link = ""
