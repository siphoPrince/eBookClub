#!/usr/bin/python3
"""Reviews models"""
from Models.parent_model import Parentmodel


class Reviews(Parentmodel):
    """reveiws class"""
    Book_id = ""
    user_id = ""
    Review_text =""
    rating = 0
