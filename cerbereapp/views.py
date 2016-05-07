# -*- coding: utf-8 -*-
from cerbereapp import app
from flask import render_template, redirect, url_for, request, render_template\
                , escape, flash, session

#from flask_wtf import Form
#from wtforms import StringField
#from wtforms.validators import DataRequired
from cerbereapp.forms import *
from functools import wraps

import cerbereapp.database as database
import cerbereapp.models as models

from flask import Flask,session, request, flash, url_for, redirect, render_template, abort ,g
from flask.ext.login import login_user , logout_user , current_user , login_required

import flask.ext.login as flask_login
from flask_login import login_required, current_user, LoginManager

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(id):
    try:
        return models.User.get(models.User.id == id)
    except:
        return None

## Login Decorator
## ==================================================
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

#@app.route('/')
#def index():
#    #return '<html><body><h1>Hello <em>world</em></h1></body></html>'
#    #return render_template('index.html')
#    if 'username' in session:
#        username=session['username']
#        return render_template("index.html", username=username)
#        #return 'Logged in as ' + username + "</br> <b><a href='/logout'>click here to log out</a></b>"
#    return "You are not logged in <br><a href='/login'></b> click here to login</b></a>"


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    email = request.form['email']
    password = request.form['password']
    registered_user = models.User.query.filter_by(email=email,password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('index'))

#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    error = None
#    if request.method == 'POST':
#        if request.form['email'] != 'admin@admin.com' or request.form['password'] != 'admin':
#            error = "Invalid credentials, please try again"
#        else:
#            session['logged_in'] = True
#            flash('Successfully logged in!', category='success')
#            return redirect(url_for('dashboard'))
#    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logged out.', category="info")
    return redirect(url_for('index'))



@app.route('/signup' , methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    user = database.User(request.form['username'] , request.form['password'],request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/employees')
def employees():
    return render_template('student.html')

@app.route('/profiles')
def profiles():
    return render_template('student.html')

@app.route('/sessions')
def sessions():
    return render_template('student.html')

@app.route('/students')
def students():
    return render_template('student.html')

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
    #db_session.rollback()
    return render_template('errors/500.html'), 500
