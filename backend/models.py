""" Models For Specific Co-op DataBase"""
from typing import List
from Industries import RoleCategory
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
    roles: Mapped[List["Role"]] = relationship(back_populates="company")


## Remember to replace the back_populates with something real from the role model BELOW. Try to understad what the parameter is meant to be and
## SqLAlchemy has a tool called ENUM that allows me to write distinct values.
class Role(Base):
    """ Role class representing distinct roles and functions"""
    __tablename__ = "roles"
    role_id:Mapped[int]=mapped_column(primary_key=True)
    title: Mapped[str]=mapped_column(String(40))
    category:Mapped[str]=mapped_column(RoleCategory)
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.company_id"))
    company:Mapped["Company"]=relationship(back_populates="roles")
