from datetime import datetime as dt

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import UniqueConstraint


from . import Base


class User(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    creation_date = Column(DateTime, default=dt.now())
    name = Column(String(30), nullable=False)
    surname = Column(String(100), nullable=False)

    __table_args__ = (UniqueConstraint('name', 'surname'),)
