from flask import jsonify, request
from tus_app import app
from tus_app.models import User


@app.route('/')
def hello_world():  # put application's code here

    return 'Hello Worldddddd!'
