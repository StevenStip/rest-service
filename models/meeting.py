from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

class meeting(object):
    __tablename__ = 'meetings'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)


def __init__(self, location, created_by):
        self.created_time = datetime.utcnow()
        self.location = location
        self.created_by_user = created_by