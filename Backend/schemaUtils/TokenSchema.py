"""
Module Name: TokenSchema.py
Author: Arun
"""
from typing import Optional

from pydantic import BaseModel
from datetime import datetime


class TokenBase(BaseModel):
    CustomerID: Optional[int]
    entry_time: datetime
    status: int
    ShopID: int


class TokenResponse(TokenBase):
    token_number: int

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),  # Convert datetime to ISO format string
        }


class UpdateTokenStatus(BaseModel):
    status: int
    id: int
    shop_id: int


class TokenCreationResponse(BaseModel):
    id: int


class TokenCustomerResponse(TokenCreationResponse):
    id: int
    entry_time: datetime


class TokenStatistics(BaseModel):
    waiting_tokens: int
    served_tokens: int

    class Config:
        orm_mode = True
