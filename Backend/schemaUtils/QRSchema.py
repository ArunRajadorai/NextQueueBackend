"""
Module Name: QRSchema.py
Author: Arun
"""
from pydantic import BaseModel


class QRCreate(BaseModel):
    qr_code: str
    shop_id: str

    class Config:
        orm_mode = True
