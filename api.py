import os, sqlite3
from  flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/v1/meetings', methods=['GET'])
def getMeetings():
    return "Hello, World!"



if __name__ == '__main__':
    app.run(debug=True)
