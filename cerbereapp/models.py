# -*- coding: utf-8 -*-
#!/usr/bin/env python

from sqlalchemy import Column, Integer, String
from cerbereapp.database import Base

## Models
## ==================================================

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(30))
    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password


class AccountType(Base):
    __tablename__ = 'account_types'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    first_name = Column(String(50))
    last_name = Column(String(50))
    profile_id = Column(Integer)


class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    profile_name = Column(String(50))


class DocumentModel(Base):
    __tablename__ = 'document_models'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    document_model_name = Column(String(50))
    warning_days = Column(Integer)
    critical_days = Column(Integer)


class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer)
    expiration_date = Column(String(50))
    document_scan = Column(Integer)
