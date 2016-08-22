from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

#Engine = create_engine('sqlite:///:memory:', echo=True)
Engine = create_engine('sqlite:///sqlalchemy_example.db', echo=True)

Base = declarative_base()

Session = sessionmaker(bind=Engine)
