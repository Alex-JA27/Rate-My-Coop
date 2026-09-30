""" Establishing Simple FastAPI connection"""
from typing import Sequence
from fastapi import Depends, FastAPI,HTTPException,Query
from models import Base,Company,Role,User,Review
from database import get_session, engine, SessionDep
from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas import CompanyOut, RoleOut,ReviewOut,CompanyIn


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

def read_roles_within_company(session:SessionDep,company_id : int)-> Sequence[Role]:
    """ Reads and reproduces all the roles within a specific company"""
    stmt = (select(Role)
            .where(Role.company_id == company_id))

    selected_roles = session.scalars(stmt).all()
    return selected_roles


@app.get("/companies/{company_id}/roles",response_model=list[RoleOut])
def get_roles(session:SessionDep,company_id:int)-> Sequence[Role]:
    """ Function to return all selected company id"""
    return read_roles_within_company(session,company_id)



def read_reviews_for_role(session:SessionDep,role_id :int)-> Sequence[Review]:
    """Reads and reproduces all the reviews about a specfic role"""
 
    stmt =(select(Review)
            .where(Review.role_id == role_id ))
    
    selected_reviews = session.scalars(stmt).all()
    return selected_reviews

@app.get("/roles/{role_id}/reviews",response_model=list[ReviewOut])
def get_review(session:SessionDep,role_id:int)-> Sequence[Review]:
    """ Function to return return all selected reviews for a role"""
    return read_reviews_for_role(session,role_id)

@app.post("/companies",response_model=CompanyOut)
def create_company(session:SessionDep,company : CompanyIn) -> Company:
    """ Should ccreate a company role/object using SQLAlchemy """
    
    stmt = select(Company).where(Company.name == company.name )
    if session.scalars(stmt).first() is None:
        new_company = Company(name = company.name)
        session.add(new_company)
        session.commit()
        return new_company
    else:
        raise HTTPException(status_code=409,detail="Company already exists")
        
        
    
    
    
    
    
