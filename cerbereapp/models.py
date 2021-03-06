# -*- coding: utf-8 -*-
#!/usr/bin/env python

from sqlalchemy import Column, Integer, String, Date, DateTime, Binary\
                    , PrimaryKeyConstraint, ForeignKeyConstraint, ForeignKey
import flask.ext.login as flask_login
from flask_login import UserMixin, current_user, login_user , logout_user \
                        , LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

import cerbereapp.database as database

## Models
## ==================================================
class User(database.Base, UserMixin):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, index=True)
    password = Column(String(250), nullable=False)
    account_type = Column(Integer, ForeignKey("account_types.id"), nullable=False)
    username = Column(String(50), unique=True)
    registered_on = Column('registered_on' , DateTime)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)
        self.account_type = 1
        self.registered_on = datetime.utcnow()

    def set_password(self , password):
        self.password = generate_password_hash(password)

    def check_password(self , password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
        #return self.username

    def __repr__(self):
        return '<User %r>' % (self.username)


class AccountType(database.Base):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'account_types'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class Employee(database.Base):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    profile_id = Column(Integer, nullable=False)


class Profile(database.Base):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    profile_name = Column(String(50), nullable=False)


class DocumentModel(database.Base):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'document_models'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    document_model_name = Column(String(50), nullable=False)
    warning_days = Column(Integer, nullable=False)
    critical_days = Column(Integer, nullable=False)


class Document(database.Base):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    document_model_id = Column(Integer, ForeignKey("document_models.id"), nullable=False, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False, index=True)
    expiration_date = Column(Date, nullable=False)
    document_scan = Column(Binary)
