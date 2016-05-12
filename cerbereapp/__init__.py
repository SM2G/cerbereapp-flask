# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Flask, session, redirect, url_for, request, render_template, escape
import configparser

app = Flask(__name__, instance_relative_config=True)

import cerbereapp.database as database
#import cerbereapp.forms as forms
import cerbereapp.models as models
#import cerbereapp.tests as tests Work in progress
import cerbereapp.views as views

app.config.from_object('config')
app.config.from_pyfile('config.py')
actual_env = 'DEV'

@app.teardown_appcontext
def shutdown_session(exception=None):
    database.db_session.remove()
