#!/usr/bin/python3
"""Storage system"""
import Models
from Models.parent_model import ParentModel, Base
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from Models.Review_model import Review
from Models.User_model import User
from Models.Category_model import Category
from Models.Books_model import Books


class Data_storage:
    """database storage"""
    __engine = None
    __session = None


