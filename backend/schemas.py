from pydantic import BaseModel,ConfigDict
from models import Company
from Industries import RoleCategory

class CompanyOut(BaseModel):
    """ Class orchestrates which parts of our company model are assecible from API using Pydantic """
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