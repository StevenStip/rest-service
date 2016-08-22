from sqlalchemy import Column, Integer, String
from controllers.dbConnector import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def __str__(self):
        return self.__repr__()

    def as_dict(self):
        obj = {'id':self.id, 'name':self.name, 'description':self.description}
        return obj

    def __repr__(self):
        return "<User(name='{name}',description='{descr}')>".format(name=self.name, descr=self.description)


if __name__ == '__main__':
    print(type(User.__table__))
    u =User('Steven', 'the boss')
    print(u)