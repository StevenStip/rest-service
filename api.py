import os, sqlite3, json
from flask import Flask, request
from controllers.userController import UserController

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/api/v1/meetings', methods=['GET'])
def getMeetings():
    return "Hello, World!"

@app.route('/api/v1/user/<id>', methods=['get'])
def getUser(id):
    ucontroller = UserController()
    user = ucontroller.getUser(id)
    return json.dumps(user.as_dict())


@app.route('/api/v1/users', methods=['GET'])
def getUsers():
    ucontroller = UserController()
    users = ucontroller.getUsers()
    result={'users':[]}
    for u in users:
        result['users'].append(u.as_dict())
        print(u)
    print(users)
    return json.dumps(result)

@app.route('/api/v1/user', methods=['PUT'])
def createUser():
    pass

@app.route('/api/v1/user/<name>', methods=['PUT'])
def putUser(name):
    print(name)
    ucontroller = UserController()

    u = ucontroller.createUser(name)
    return "succes, I guess...!"


if __name__ == '__main__':
    app.run(debug=True)
