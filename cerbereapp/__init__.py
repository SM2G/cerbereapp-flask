# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Flask, session, redirect, url_for, request, render_template, escape
import flask.ext.login as flask_login
import configparser

app = Flask(__name__, instance_relative_config=True)

import cerbereapp.views
import cerbereapp.database

app.config.from_object('config')
app.config.from_pyfile('config.py')
actual_env = 'DEV'

app.secret_key = 'justasimplerandomstring'

login_manager = flask_login.LoginManager()
login_manager.init_app(app)


if __name__=='__main__':
    app.run
