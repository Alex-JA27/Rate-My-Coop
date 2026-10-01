""" Establishing Simple FastAPI connection"""
from typing import Sequence
from fastapi import FastAPI,HTTPException
from models import Base,Company,Role,User,Review
from database import engine, SessionDep
from sqlalchemy import select
from schemas import CompanyOut, RoleOut,ReviewOut,CompanyIn,RoleIn,ReviewIn


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
    """ Should ccreate a company row/object using SQLAlchemy """
    stmt = select(Company).where(Company.name == company.name.strip() )
    if session.scalars(stmt).first() is None:
        new_company = Company(name = company.name)
        session.add(new_company)
        session.commit()
        return new_company
    else:
        raise HTTPException(status_code=409,detail="Company already exists")

@app.post("/roles",response_model=RoleOut)
def create_role(session:SessionDep,role:RoleIn)-> Role:
    """Should create a Role row/Object using SqlAlchemy"""
    stmt = select(Role).where(Role.company_id == role.company_id,Role.title == role.title)


    if session.get(Company,role.company_id) is None:
        raise HTTPException(status_code=404,detail="This company dosen't exist")

    if session.scalars(stmt).first() is None:
        new_role = Role(title = role.title.strip(),category =
                        role.category,company_id = role.company_id)
        session.add(new_role)
        session.commit()
        return new_role
    else:
        raise HTTPException(status_code=409,
                            detail="This role already exists for the selected company")


@app.post("/reviews",response_model=ReviewOut)
def create_review(session:SessionDep,review:ReviewIn)-> Review:
    """ Should create a new review Row/Object using SQLAlchemy"""


    if session.get(Role,review.role_id) is None:
        raise HTTPException(status_code=404,detail="This role dosen't exist")

    if session.get(User,review.user_id) is None:
        raise HTTPException(status_code=404)

    term_text = f"{review.term.season.value}{review.term.year}"

    new_review = Review(star_rating = review.star_rating,term = term_text,
                        review_body = review.review_body,role_id = review.role_id,
                        user_id = review.user_id,anonymous_flag = review.anonymous_flag)

    session.add(new_review)
    session.commit()
    return new_review
