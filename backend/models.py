""" Models For Specific Co-op DataBase"""
from typing import List
from sqlalchemy import ForeignKey,String
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship

class Base(DeclarativeBase):
    """ Base Class for Tables"""
    pass 


class Company(Base):
    """ Company Class representing companies table"""
    __tablename_ = "companies"
    company_id : Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]= mapped_column(String(40))
    roles: Mapped[List["Role"]] = relationship(back_populates="??")


