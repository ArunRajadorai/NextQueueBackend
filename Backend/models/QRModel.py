"""
Module Name: QRModel.py
Author: Arun
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from Backend.configs.Database import Base


class QR(Base):
    __tablename__ = "qrcode"
    Id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Qr_code = Column(String(100), index=True)
    ShopID = Column(Integer, ForeignKey('shop.ShopID'), index=True)
    CreatedAt = Column(String(100), index=True)
    shop = relationship("Shop", back_populates="qr")
