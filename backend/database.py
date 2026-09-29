""" SQL Database connection Code"""
from collections.abc import Generator
from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from fastapi import Depends

engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/ratemycoop",echo=True)

SESSION_LOCAL = sessionmaker(bind=engine)




def get_session()-> Generator[Session]:
     """ Retrieves a brandnew session for each FastAPI connnection"""
     db = SESSION_LOCAL()
     try:
         yield db
     finally:
        db.close()
       
SessionDep = Annotated[Session ,Depends(get_session)]
