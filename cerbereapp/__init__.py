# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Flask, session, redirect, url_for, request, render_template, escape
import configparser

app = Flask(__name__, instance_relative_config=True)

import cerbereapp.database
import cerbereapp.forms
import cerbereapp.models
import cerbereapp.views

app.config.from_object('config')
app.config.from_pyfile('config.py')
actual_env = 'DEV'


from cerbereapp.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
