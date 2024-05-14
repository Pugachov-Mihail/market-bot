import datetime

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Integer, ForeignKey, DATETIME, String, Column, Boolean

Base = declarative_base()


class Finance(Base):
    __tablename__ = "finance"

    name_operation = Column()
