from sqlalchemy import create_engine
from .base import Base
from sqlalchemy.orm import sessionmaker
from . import task

engine = create_engine('sqlite:///:memory:')

Base.metadata.create_all(bind=engine, checkfirst=True)

Session = sessionmaker(bind=engine)
session = Session()
