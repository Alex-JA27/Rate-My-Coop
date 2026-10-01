""" Pydantic Models used to define data to and from users"""
from pydantic import BaseModel,ConfigDict,Field,field_validator
from Industries import RoleCategory, Seasons
from datetime import datetime

class CompanyOut(BaseModel):
    """ Class orchestrates which parts of our company model 
    are assecible from API using Pydantic """
    model_config = ConfigDict(from_attributes=True)
    company_id: int
    name :str

class RoleOut(BaseModel):
    """ Class orchestrates which parts of the role model are accesible from API using Pydantic """
    model_config = ConfigDict(from_attributes=True)
    role_id: int
    title: str
    category : RoleCategory

class ReviewOut(BaseModel):
    """ Class orchestrates which parts of the review model are accesible from API using Pydantic"""
    model_config = ConfigDict(from_attributes=True)
    review_id : int
    star_rating : float
    term : str
    review_body : str
    anonymous_flag : bool


class CompanyIn(BaseModel):
    """ Class orchestrates which part of the company model should be sent in from the end user"""
    name : str

class RoleIn(BaseModel):
    """ Class orchestrates which part of the role model should be sent in from the end user """
    title : str
    category : RoleCategory
    company_id : int

class Term(BaseModel):
    "Class decides whats  dictates a  valid term"

    season: Seasons
    year : int = Field(ge=2000)
    @field_validator("year")
    @classmethod
    def year_check(cls,value:int)-> int:
        """ checks whether the given year value is valid """
        if value > datetime.now().year:
            raise ValueError("That year is invalid")
        return value 

class ReviewIn(BaseModel):
    """ Class orchestrates which part of the role model should be sent in from the end user """
    star_rating :float =  Field(ge= 1 ,le= 5,multiple_of= 0.5)
    term: Term
    review_body : str = Field(max_length= 1500 )
    role_id : int
    user_id : int
    anonymous_flag :bool = True

   
