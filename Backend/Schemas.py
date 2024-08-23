from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

"Author @Arun"


class User(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True


class UserSignIn(BaseModel):
    userName: str
    password: str


class UserSignInResponse(BaseModel):
    token: str
    user: dict[str, str | list[str]] = {
        "userName": str,
        "authority": List[str],
        "avatar": str,
        "email": str
    }


class UserSignupResponse(BaseModel):
    status: int
    statusText: str


class CustomerBase(BaseModel):
    phoneNumber: str


class CustomerCreate(BaseModel):
    mobileNumber: str
    shopId: int


class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True


class QueueBase(BaseModel):
    Token_number: int
    CustomerID: int
    Entry_time: datetime
    status: str


class QueueCreate(QueueBase):
    pass


class TokenSelect(BaseModel):
    token_id: int


class Queue(QueueBase):
    pass

    class Config:
        orm_mode = True


class Dealer(BaseModel):
    DealerID: int
    DealerName: str
    DealerAddress: str
    DealerPhone: str
    status: str
    statusText: str


class DealerUpdate(BaseModel):
    DealerID: Optional[int]
    DealerName: Optional[str]
    DealerAddress: Optional[str]
    DealerPhone: Optional[str]
    status: Optional[str]
    statusText: Optional[str]


class Shop(BaseModel):
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


class ShopResponse(Shop):
    status: str
    statusText: str
