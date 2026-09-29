from pydantic import BaseModel,ConfigDict

class CompanyOut(BaseModel):
    """ Class orchestrates which parts of our models are assecible from API using Pydantic """
    model_config = ConfigDict(from_attributes=True)
    company_id: int
    name :str 