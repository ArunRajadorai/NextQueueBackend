"""
Module Name: CompanyModel.py
Author: Arun
"""
from sqlalchemy import Integer, Column, String

from Backend.configs.Database import Base


class Company(Base):
    __tablename__ = "company"
    CompanyID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    CompanyName = Column(String(100), index=True)
    CompanyOwnerName = Column(String(100), index=True)
    PhoneNumber = Column(String(100), index=True)
    Email = Column(String(100), index=True)
    Address = Column(String(100), index=True)
    Address2 = Column(String(100), index=True)
    Town = Column(String(100), index=True)
    PostalCode = Column(String(100), index=True)
    State = Column(String(100), index=True)
    Country = Column(String(100), index=True)