from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from Backend.configs.Database import Base


class Auth(Base):
    __tablename__ = 'auth_token'
    Authid = Column(Integer, primary_key=True, autoincrement=True)
    App_name = Column(String(50), index=True)
    App_password = Column(String(50), index=True)
    access_token = Column(String(255), index=True)
    request_time = Column(DateTime, index=True, default=datetime.now)

