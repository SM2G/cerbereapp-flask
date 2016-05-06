# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Flask
from sqlalchemy import create_engine
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

#connection = pymysql.connect(host = config['DEV']['host'],
#                             user = config['DEV']['user'],
#                             password = config['DEV']['password'],
#                             db = config['DEV']['db'],
#                             charset = 'utf8mb4',
#                             cursorclass = pymysql.cursors.DictCursor)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


# Create tables.
def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import cerbereapp.models
    Base.metadata.create_all(bind=engine)
