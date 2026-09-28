""" Establishing Simple FastAPI connection"""
from typing import Annotated
from fastapi import FastAPI
from fastapi import Depends, FastAPI,HTTPException,Query
from models import Base
from database import get_session, engine, SessionDep
from sqlalchemy.orm import Session



def create_db_and_tables()-> None:
    """ Function Creates all the tables from models """
    Base.metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
def on_startup()-> None:
    """ method Runs on every connection of the API """
    create_db_and_tables()

