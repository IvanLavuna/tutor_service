import random
import string
from passlib.apps import custom_app_context as pwd_context
from sqlalchemy import Column, Integer, String, ForeignKey, BLOB, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

BaseModel = declarative_base()


# secret key to create and verify tokens
secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))


class User(BaseModel):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(55), unique=False, nullable=False)
    last_name = Column(String(55), unique=False, nullable=False)
    location = Column(String(55), unique=False, nullable=True)
    username = Column(String(55), unique=True, nullable=False)
    password_hash = Column(String(300), unique=False, nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    phone = Column(String(15), unique=True, nullable=True)
    photo = Column(BLOB, unique=False, nullable=True, default="..")  # TODO: create default blob object
    role = Column(Enum('Tutor', 'Admin', 'Client'), unique=False, nullable=False, default='Client')

    def __repr__(self):
        return f"User('{self.username}','{self.firstname}','{self.lastname}','{self.email}','{self.phone_number}')"

