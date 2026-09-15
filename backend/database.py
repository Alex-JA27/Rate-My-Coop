""" SQL Database connection Code"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/ratemycoop",echo=True)

SESSION = sessionmaker(bind=engine)

