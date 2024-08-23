"""
Module Name: ShopSchema.py
Author: Arun
"""
from typing import Optional

from pydantic import BaseModel, Field


class ShopRequest(BaseModel):
    shop_id: int


class ShopCreate(BaseModel):
    shopName: str
    shopOwnername: str
    shopAddress1: str
    shopAddress2: Optional[str]
    shopTown: str
    shopState: str
    country: str
    shopPostalcode: str
    shopEmail: str
    shopPhone: str
    company: int

    class Config:
        from_attributes = True


class ShopResponse(BaseModel):
    shopID: int = Field(alias='ShopID')
    shopName: str = Field(alias='ShopName')
    shopOwnername: str = Field(alias='ShopOwnerName')
    shopPhone: str = Field(alias='PhoneNumber')
    shopEmail: str = Field(alias='Email')
    shopAddress1: str = Field(alias='Address')
    shopAddress2: Optional[str] = Field(alias='Address2')
    shopTown: str = Field(alias='Town')
    shopPostalcode: str = Field(alias='PostalCode')
    shopState: str = Field(alias='State')
    country: str = Field(alias='Country')

    class Config:
        from_attributes = True


class ShopDelete(BaseModel):
    id: int
