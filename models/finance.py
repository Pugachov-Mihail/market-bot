import datetime

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Integer, ForeignKey, DATETIME, String, Column, Boolean

Base = declarative_base()


class Operation(Base):
    __tablename__ = "operation"

    id = Column(Integer, primary_key=True, autoincrement=True)
    operation_name = Column(String, unique=True)
    name = relationship("Finance", back_populates="name_operation")


class Finance(Base):
    __tablename__ = "finance"

    id = Column(Integer, primary_key=True, autoincrement=True)
    operation_id = Column(ForeignKey('operation.id'))
    name_operation = relationship("Operation", back_populates="name")
    create_datetime = Column(DATETIME, default=datetime.datetime.now())
    balance = Column(Integer)
