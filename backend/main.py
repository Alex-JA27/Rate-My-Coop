""" Establishing Simple FastAPI connection"""
from typing import Sequence
from fastapi import Depends, FastAPI,HTTPException,Query
from models import Base,Company,Role,User,Review
from database import get_session, engine, SessionDep
from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas import CompanyOut


def create_db_and_tables()-> None:
    """ Function Creates all the tables from models """
    Base.metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
def on_startup()-> None:
    """ method Runs on every connection of the API """
    create_db_and_tables()

def read_all_companies(session:SessionDep)-> Sequence[Company]:
    """ Reads and reproduces all the companies in our database"""
    companies = session.scalars(select(Company)).all()
    return companies

@app.get("/companies",response_model=list[CompanyOut])
def get_companies(session:SessionDep)-> Sequence[Company]:
    """ Function to return the list of companies"""
    return read_all_companies(session)
