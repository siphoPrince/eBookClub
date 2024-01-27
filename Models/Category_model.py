#!/usr/bin/python3
"""Category model"""
from Models.parent_model import Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base


class Category(Base):
    """category class with f.f attr
    category number, name
    """
    __tablename__ = 'Category'
    category_number = Column(Integer, primary_key =True, nullable=False, default=0)
    category_name = Column(String(128), nullable=False)
