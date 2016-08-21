from controllers.userController import userController

if __name__ == '__main__':
    userController.createUser('japie2')
    r = userController.getUsers()
    for user in r:
        print(user)