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
        return u

    def getUsers(self):
        return self.session.query(User).order_by(User.id)


userController = UserController()
userController.createUser('Steven')
userController.createUser('Fiona')
userController.session.commit()
users = userController.getUsers()
for u in users:
    print(u)

