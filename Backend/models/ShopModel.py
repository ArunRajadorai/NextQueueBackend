"""
Module Name: ShopModel.py
Author: Arun
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from Backend.configs.Database import Base


class Shop(Base):
    __tablename__ = "shop"
    ShopID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ShopName = Column(String(100), index=True)
    ShopOwnerName = Column(String(100), index=True)
    CompanyID = Column(Integer, ForeignKey('company.CompanyID'), index=True)
    PhoneNumber = Column(String(100), index=True)
    Email = Column(String(100), index=True)
    Address = Column(String(100), index=True)
    Address2 = Column(String(100), index=True)
    Town = Column(String(100), index=True)
    PostalCode = Column(String(100), index=True)
    State = Column(String(100), index=True)
    Country = Column(String(100), index=True)
    qr = relationship("QR", back_populates="shop")
