# -*- coding: utf-8 -*-

from flask import Flask, session, redirect, url_for, request, render_template, escape
app = Flask(__name__)
app.secret_key = 'justasimplerandomstring'

@app.route('/')
#Landing page
def index():
    #return '<html><body><h1>Hello <em>world</em></h1></body></html>'
    #return render_template('index.html')
    if 'username' in session:
        username=session['username']
        return render_template("index.html")
        return 'Logged in as ' + username + '</br>' + \
        "<b><a href='/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href='/login'></b>" + \
"click here to login</b></a>"

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
#Graph dashboard

@app.route('/account')
#Personnal account informations

@app.route('/new_session')
#Initialize a new session

@app.route('/sessions')
#Review all past sessions (mostly read only)

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


if __name__=='__main__':
    app.run(debug=True)
