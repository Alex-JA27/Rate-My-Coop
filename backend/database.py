""" SQL Database connection Code"""
from dotenv import load_dotenv
import os
from collections.abc import Generator
from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from fastapi import Depends

load_dotenv()
password = os.getenv("DB_PASSWORD")

engine = create_engine(f"mysql+pymysql://root:{password}@127.0.0.1:3306/ratemycoop",echo=True)

SESSION_LOCAL = sessionmaker(bind=engine)




def get_session()-> Generator[Session]:
    """ Retrieves a brandnew session for each FastAPI connnection"""
    db = SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close()

SessionDep = Annotated[Session ,Depends(get_session)]
