import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import objectid
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
