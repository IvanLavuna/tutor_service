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
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(55), unique=False, nullable=False)
    last_name = Column(String(55), unique=False, nullable=False)
    location = Column(String(55), unique=False, nullable=True)
    username = Column(String(55), unique=True, nullable=False)
    password_hash = Column(String(300), unique=False, nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    phone = Column(String(15), unique=True, nullable=True)
    photo = Column(BLOB, unique=False, nullable=True)  # TODO: create default blob object
    role = Column(Enum('Tutor', 'Admin', 'Client'), unique=False, nullable=False, default='Client')

    def __repr__(self):
        return f"User('{self.username}','{self.firstname}','{self.lastname}','{self.email}','{self.phone_number}')"


class CV(BaseModel):
    __tablename__ = 'CV'

    id = Column(Integer, primary_key=True)
    text = Column(String(2000), unique=False, nullable=False)
    rating = Column(float, unique=False, nullable=True)

    user_id = Column(Integer, ForeignKey('User.id'), unique=True, nullable=False)

    user = relationship(User)

    def __repr__(self):
        return f"CV('{self.text}','{self.rating}')"


class Subject(BaseModel):
    __tablename__ = 'Subject'

    id = Column(Integer, primary_key=True)
    name = Column(
        Enum('English', 'Germany', 'History', 'Astronomy', 'Math', 'Chemistry', 'Physics', 'Biology', 'Literature'),
        unique=False, nullable=True)

    cv_id = Column(Integer, ForeignKey('CV.id'), unique=True, nullable=False)
    cv_user_id = Column(Integer, ForeignKey('CV.User.id'), unique=False, nullable=False)

    cv = relationship(CV)
    cv_user = relationship(User)

    def __repr__(self):
        return f"Subject('{self.name}')"


class Review(BaseModel):
    __tablename__ = 'Review'

    id = Column(Integer, primary_key=True)
    text = Column(String(1000), unique=False, nullable=False)
    mark = Column(Integer, unique=False, nullable=False, default=0)
    user_id=Column(Integer,ForeignKey('User.id'),unique=False,nullable=False)
    def __repr__(self):
        return f"Review('{self.text}','{self.mark}')"
