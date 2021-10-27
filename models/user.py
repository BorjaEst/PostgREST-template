from datetime import datetime as dt

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from . import Base


class User(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    creation_date = Column(DateTime, default=dt.now())
    name = Column(String(30))
    fullname = Column(String)
