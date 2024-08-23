"""
Module Name: CustomerSchema.py
Author: Arun
"""
from typing import Optional

from pydantic import BaseModel


class CustomerCreate(BaseModel):
    mobileNumber: Optional[str] = None
    shopId: int
