from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from Backend.configs.Database import Base
from datetime import datetime
import enum

"Author @Arun"
class StatusEnum(str, enum.Enum):
    waiting = "waiting"
    approved = "approved"
    served = "served"


# class Customer(Base):
#     __tablename__ = "customer"
#     CustomerID = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     phoneNumber = Column(String, index=True)


class Queue(Base):
    __tablename__ = "queue"
    Token_number = Column(Integer, primary_key=True, index=True, autoincrement=True)
    CustomerID = Column(Integer, ForeignKey("customer.CustomerID"))
    Entry_time = Column(DateTime, default=datetime.utcnow)
    status = Column(Enum(StatusEnum), default=StatusEnum.waiting)
    customer = relationship("Customer")


class User(Base):
    __tablename__ = "user"
    UserID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    UserName = Column(String(100), index=True)
    UserPassword = Column(String(100), index=True)
    UserEmail = Column(String(100), index=True)
    UserPhone = Column(String(100), index=True)


class Dealers(Base):
    __tablename__ = "dealers"
    DealerID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    DealerName = Column(String(100), index=True)
    DealerPhone = Column(String(100), index=True)
    DealerEmail = Column(String(100), index=True)
    DealerAddress = Column(String(100), index=True)

# class Shop(Base):
#     __tablename__ = "shop"
#     ShopID = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     ShopName = Column(String(100), index=True)
#     ShopOwnerName = Column(String(100), index=True)
#     PhoneNumber = Column(String(100), index=True)
#     Email = Column(String(100), index=True)
#     Address = Column(String(100), index=True)
#     Address2 = Column(String(100), index=True)
#     Town = Column(String(100), index=True)
#     PostalCode = Column(String(100), index=True)
#     State = Column(String(100), index=True)
#     Country = Column(String(100), index=True)
#
# class Company(Base):
#     __tablename__ = "company"
#     CompanyID = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     CompanyName = Column(String(100), index=True)
#     CompanyOwnerName = Column(String(100), index=True)
#     PhoneNumber = Column(String(100), index=True)
#     Email = Column(String(100), index=True)
#     Address = Column(String(100), index=True)
#     Address2 = Column(String(100), index=True)
#     Town = Column(String(100), index=True)
#     PostalCode = Column(String(100), index=True)
#     State = Column(String(100), index=True)
#     Country = Column(String(100), index=True)


