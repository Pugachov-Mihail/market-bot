import datetime

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Integer, ForeignKey, DATETIME, String, Column, Boolean

Base = declarative_base()


class Goods(Base):
    __tablename__ = "good"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sales_price = Column(Integer)
    purchase_price = Column(Integer)
    count = Column(Integer)
    create_date = Column(DATETIME, default=datetime.datetime.now())
    markets = Column(ForeignKey("market.id"))
    status = Column(Boolean, default=False, comment="Продан товар")


class Markets(Base):
    __tablename__ = "market"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    url_id = Column(ForeignKey("link.id"))


class Links(Base):
    __tablename__ = "link"

    id = Column(Integer, primary_key=True)
    url = Column(String)
