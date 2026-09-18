""" Models For Specific Co-op DataBase"""
from typing import List
from Industries import RoleCategory
from sqlalchemy import ForeignKey,String, Numeric
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


class Role(Base):
    """ Role class representing distinct roles and functions"""
    __tablename__ = "roles"
    role_id:Mapped[int]=mapped_column(primary_key=True)
    title: Mapped[str]=mapped_column(String(40))
    reviews:Mapped[List[Review]]=relationship(back_populates="role")
    category:Mapped[str]=mapped_column(RoleCategory)
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.company_id"))
    company:Mapped["Company"]=relationship(back_populates="roles")

class Review(Base):
    """ Review class represents a single review written by a user """
    __tablename__="reviews"
    review_id: Mapped[int]=mapped_column(primary_key=True)
    star_rating:Mapped[float]=mapped_column(Numeric(precision=3,scale=2))
    term:Mapped[str]=mapped_column(String(50))
    review_body:Mapped[str]=mapped_column(String(250))
    anonymous_flag:Mapped[bool]=mapped_column()## How about booleans?
    role_id:Mapped[int]=mapped_column(ForeignKey("roles.role_id"))
    role: Mapped["Role"]=relationship(back_populates="reviews")
    user_id:Mapped[int]=mapped_column(ForeignKey("users.user_id"))
    user:Mapped["User"]=relationship(back_populates="user")## Placeholder until user class is implemented below
    