from database import engine
from models import Base
from models import User
from models import Company
from models import Role
from models import Review


Base.metadata.create_all(engine)