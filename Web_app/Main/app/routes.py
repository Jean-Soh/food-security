from flask import render_template
from app import application

@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html', title='DTP web app')

@application.route('/ex1')
def exercise1():
    return render_template('ex1.html', title='Page 1')

@application.route('/ex2')
def exercise2():
    return render_template('ex2.html', title='Page 2')