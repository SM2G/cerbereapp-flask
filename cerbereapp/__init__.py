# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Flask, session, redirect, url_for, request, render_template, escape
from flask.ext.sqlalchemy import SQLAlchemy
import configparser
import pymysql

app = Flask(__name__, instance_relative_config=True)

import cerbereapp.views


config = configparser.ConfigParser()
config.read('instance/db-config.ini')

app.config.from_object('config')
app.config.from_pyfile('config.py')
actual_env = 'DEV'

app.secret_key = 'justasimplerandomstring'

import flask.ext.login as flask_login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


if __name__=='__main__':
    app.run
