from controllers.userController import UserController

if __name__ == '__main__':
    uc = UserController()
    uc.createUser('japie2')
    r = uc.getUsers()
    for user in r:
        print(user)