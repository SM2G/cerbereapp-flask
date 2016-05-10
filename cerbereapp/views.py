# -*- coding: utf-8 -*-
from cerbereapp import app
from flask import render_template, redirect, url_for, request, render_template\
                , escape, flash, session, Flask, abort, g

from cerbereapp.forms import *
from functools import wraps
from datetime import datetime
#from werkzeug.security import generate_password_hash, check_password_hash

import flask.ext.login as flask_login
from flask_login import login_required, current_user, login_user , logout_user \
                        , LoginManager

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

import cerbereapp.database as database
import cerbereapp.models as models

## Login Decorator
## ==================================================

@login_manager.user_loader
def load_user(id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve
    """
    return  models.User.query.get(id)
    #return models.User.get(models.User.id == id)
    #except:
    #    return None

@app.before_request
def before_request():
    g.user = current_user

#def login_required(f):
#    @wraps(f)
#    def wrap(*args, **kwargs):
#        if 'logged_in' in session:
#            return f(*args, **kwargs)
#        else:
#            flash('You need to login first', category='info')
#            return redirect(url_for('login'))
#    return wraps

## Routes
## ==================================================
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login',methods=['GET','POST'])
def login():
    """
    Authenticate users.
    """
    if request.method == 'GET':
        return render_template('login.html')
    email = request.form['email']
    password = request.form['password']
    remember_me = False
    if 'remember_me' in request.form:
        remember_me = True
    registered_user = models.User.query.filter_by(email=email).first()
    if registered_user is None:
        flash('Invalid username' , category='danger')
        return redirect(url_for('login'))
    if not registered_user.check_password(password):
        flash('Invalid Password' , category='danger')
        return redirect(url_for('login'))
    login_user(registered_user, remember = remember_me)
    flash('Logged in successfully', category='success')
    return redirect(request.args.get('next') or url_for('dashboard'))


@app.route('/logout')
def logout():
    #session.pop('logged_in', None)
    logout_user()
    flash('Successfully logged out.', category="info")
    return redirect(url_for('index'))


@app.route('/signup' , methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    user = models.User(request.form['username']
                    , request.form['email']
                    , request.form['password']
                    , request.form['password_check'])
    if user.password != user.password_check
        flash('Passwords mismatch' , category='danger')
        return redirect(url_for('signup'))
    database.db_session.add(user)
    database.db_session.commit()
    flash('User successfully registered', category='success')
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/employees')
@login_required
def employees():
    return render_template('student.html')


@app.route('/employee/<int:employee_id>')
@login_required
def employees():
    return render_template('student.html')


@app.route('/profiles')
@login_required
def profiles():
    return render_template('profiles.html')


@app.route('/profile/<int:profile_id>')
@login_required
def employees():
    return render_template('student.html')


@app.route('/document_models')
@login_required
def sessions():
    return render_template('document_models.html')


@app.route('/document_model/<int:document_model_id>')
@login_required
def sessions():
    return render_template('document_models.html')


@app.route('/student_result', methods=['POST', 'GET'])
def student_result():
    if request.method=='POST':
        result=request.form
        return render_template("table.html", result=result)


@app.route('/hello/<int:score>')
def hello_name(score):
    return render_template('hello.html', marks = score)


@app.route('/result')
def result():
    dict={'Olga':55,'Anya':24,'Tania':26,'Ivana':32,'Sonia':28,'Pussy':35,'Plenty':44}
    return render_template('table.html', result=dict)


@app.route('/account/<name>')
@login_required
def account(name):
    return 'Welcome %s!' % name


@app.route('/employee/<name>')
@login_required
def success(name):
    return 'Welcome %s!' % name


## Errors
## ==================================================
@app.errorhandler(401)
def not_found_error(error):
    flash('You must login first.', category='info')
    return render_template('login.html'), 401

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db_session.rollback()
    return render_template('errors/500.html'), 500
