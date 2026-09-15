""" SQL Database connection Code"""
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/ratemycoop",echo=True)

connection = engine.connect()


