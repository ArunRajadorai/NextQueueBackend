"""
Module Name: TokenModel.py
Author: Arun
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, DateTime, func
from sqlalchemy.orm import relationship

from Backend.configs.Database import Base


class Token(Base):
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    CustomerID = Column(Integer, ForeignKey('customer.CustomerID'), index=True)
    entry_time = Column(TIMESTAMP, default=datetime.now(), index=True)
    status = Column(Integer, default=0)  # Changed to String for status
    ShopID = Column(Integer, ForeignKey('shop.ShopID'), index=True)
    token_number = Column(Integer, nullable=False)
    last_updated = Column(DateTime, default=func.now())


class TokenSequence(Base):
    __tablename__ = 'token_sequence'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    ShopID = Column(Integer, ForeignKey('shop.ShopID'), index=True)
    LastTokenNumber = Column(Integer, default=0)
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now())
