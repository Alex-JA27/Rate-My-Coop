""" Models For Specific Co-op DataBase"""
from typing import List
from Industries import RoleCategory
from sqlalchemy import ForeignKey,String, Numeric
from sqlalchemy import Enum
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship

class Base(DeclarativeBase):
    """ Base Class for Tables"""



class Company(Base):
    """ Company Class representing companies table"""
    __tablename__ = "companies"
    company_id : Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]= mapped_column(String(40),unique=True)
    roles: Mapped[List["Role"]] = relationship(back_populates="company")


class Role(Base):
    """ Role class representing distinct roles and functions"""
    __tablename__ = "roles"
    role_id:Mapped[int]=mapped_column(primary_key=True)
    title: Mapped[str]=mapped_column(String(40),unique=True)
    reviews:Mapped[List[Review]]=relationship(back_populates="role")
    category:Mapped[RoleCategory]=mapped_column(Enum(RoleCategory))
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.company_id"),unique=True)
    company:Mapped["Company"]=relationship(back_populates="roles")

class Review(Base):
    """ Review class represents a single review written by a user """
    __tablename__="reviews"
    review_id: Mapped[int]=mapped_column(primary_key=True)
    star_rating:Mapped[float]=mapped_column(Numeric(precision=3,scale=2))
    term:Mapped[str]=mapped_column(String(50))
    review_body:Mapped[str]=mapped_column(String(1500))
    anonymous_flag:Mapped[bool]=mapped_column()## How about booleans?
    role_id:Mapped[int]=mapped_column(ForeignKey("roles.role_id"))
    role: Mapped["Role"]=relationship(back_populates="reviews")
    user_id:Mapped[int]=mapped_column(ForeignKey("users.user_id"))
    user:Mapped["User"]=relationship(back_populates="reviews")


class User(Base):
    """ User class represents a single user and their own unique credentials"""
    __tablename__="users"
    user_id: Mapped[int] = mapped_column(primary_key=True)
    reviews:Mapped[List["Review"]] = relationship(back_populates="user")
    clerk_user_id:Mapped[str] = mapped_column(String(255),unique=True)
