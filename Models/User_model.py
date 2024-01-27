#!/usr/bin/python3
"""User model"""
from Models.parent_model import Parentmodel, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class User(Parentmodel, Base):
    """user class"""
    __tablename__ = 'User'
    name = Column(String(128), nullable=True)
    surname = Column(String(128), nullable=True)
    email = Column(String(128), nullable=True)
    password = Column(String(128), nullable=True)
