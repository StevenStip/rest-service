from models.user import User
from controllers.dbConnector import Engine, Base, Session

"""To be used as a singleton for creating, storing and getting users
"""


class UserController():
    def __init__(self):
        Base.metadata.create_all(Engine)
        self.session = Session()


    def createUser(self, name):
        u = User(name)
        self.session.add(u)
        self.session.commit()
        return u

    def getUsers(self):
        r = self.session.query(User).order_by(User.id)
        print(type(r))
        for user in r:
            print("found")
            print(user)
        return [x for x in r]

    def getUser(self, id=None, name=None):
        if id is not None:
            pass


#userController = UserController()

if __name__ == '__main__':
    userController.createUser('Steven')
    userController.createUser('Fiona')
    userController.session.commit()
    users = userController.getUsers()
    for u in users:
        print(u)

