# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Flask
from sqlalchemy import create_engine, MetaData, select, insert, update, delete
from sqlalchemy.orm import scoped_session, sessionmaker
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
import pymysql
import configparser
config = configparser.ConfigParser()
config.read('instance/db-config.ini')
app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy(app)

engine = create_engine("mysql+pymysql://" + config['DEV']['user']
                        + ":"
                        + config['DEV']['password']
                        + "@"
                        + config['DEV']['host']
                        + "/"
                        + config['DEV']['db'], encoding='utf8', echo = True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


## Index naming convention
## ==================================================
convention = {
  "ix": 'ix_%(column_0_label)s',
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(constraint_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

# Create tables.
def init_db():
    """
    Import all modules here that might define models.
    They will be registered properly on the metadata.
    Otherwise you will have to import them first before calling init_db()
    """
    import cerbereapp.models
    Base.metadata.create_all(bind=engine)

def seed_db():
    """
    Injects sample data into the database.

    Use this to populate the database with some sample data.
    """
    import cerbereapp.models as models
    con = engine.connect()
    con.execute(models.account_type.insert(), [
        {'Guest'},
        {'Premium'},
        {'Free'}])
    db_session.execute(models.profiles.insert(), [
        {'user_id': 1, 'profile_name' : '1recon'},
        {'user_id': 1, 'profile_name' : '1medic'},
        {'user_id': 2, 'profile_name' : '2recon'},
        {'user_id': 2, 'profile_name' : '2medic'}])
    #db_session.execute(models.users.insert(), username='Robert', email='robert@cerbereapp.com', password='pbkdf2:sha1:1000$6b3BzWNu$b143b5ad6599fb04c97dc603aba70d1cdfa18c00')
    db_session.commit()
