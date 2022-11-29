from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class ClientData(base):
    __tablename__ = 'tbl_client_data'

    title = Column(String, primary_key=True)
    director = Column(String)
    year = Column(String)


class Transaction(base):
    __tablename__ = 'tbl_transaction'
