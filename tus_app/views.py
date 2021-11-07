from flask import jsonify, request
from tus_app import app, db_session
from tus_app.models import User, Enum
from flask_httpauth import HTTPBasicAuth
from flask import g
from functools import wraps

session = db_session()

auth = HTTPBasicAuth()


@app.route('/')
def hello_world():  # put application's code here
    user = User(first_name="Ivan", last_name="Manchur", location="Ukraine", username="LaVuna47",
            password_hash="1111", email="lavuna@gmail.com", role=Enum("CLient"))
    session.add(user)
    session.commit()
    return "He!"