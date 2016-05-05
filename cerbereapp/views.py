# -*- coding: utf-8 -*-

from cerbereapp import app
from flask import render_template, redirect, url_for, request, render_template, escape, flash
from flask_login import login_required, current_user

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


## Routes
## ==================================================
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dashboard')
@login_required
def account():
    return render_template("account.html")

#@app.route('/')
#def index():
#    #return '<html><body><h1>Hello <em>world</em></h1></body></html>'
#    #return render_template('index.html')
#    if 'username' in session:
#        username=session['username']
#        return render_template("index.html", username=username)
#        #return 'Logged in as ' + username + "</br> <b><a href='/logout'>click here to log out</a></b>"
#    return "You are not logged in <br><a href='/login'></b> click here to login</b></a>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template("login.html")


@app.route('/logout')
def logout():
    # remove username from session
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('student.html')

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

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s!' % name


## Errors
## ==================================================
@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404
