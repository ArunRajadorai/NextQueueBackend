"""
Module Name: CustomerModel.py
Author: Arun
"""
from sqlalchemy import Column, Integer, String

from Backend.configs.Database import Base


class Customer(Base):
    __tablename__ = 'customer'
    CustomerID = Column(Integer, primary_key=True, index=True)
    phoneNumber = Column(String, unique=True, index=True)