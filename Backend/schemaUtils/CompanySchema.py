# Backend/schemaUtils/CompanySchema.py
from pydantic import BaseModel
from typing import Optional


class CompanyCreate(BaseModel):
    name: str
    directorname: str
    address1: str
    address2: Optional[str] = None
    town: str
    state: str
    country: str
    postalcode: str
    email: str
    phone: str


class CompanyDelete(BaseModel):
    id: int


class CompanyResponse(BaseModel):
    id: int
    name: str
    directorname: str
    address1: str
    address2: Optional[str] = None
    town: str
    state: str
    country: str
    postalcode: str
    email: str
    phone: str

    class Config:
        from_attributes = True  # Use the new config option for Pydantic V2
