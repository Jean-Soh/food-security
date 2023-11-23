from flask import render_template
from app import application

dark = True

@application.route('/')
@application.route('/index')
def index():
    if dark == True:
        return render_template('index.html', title='Mini Project 1 Home')
    return render_template('index.html', title='Mini Project 1 Home')

@application.route('/ex1')
def exercise1():
    if dark == True:
        return render_template('ex1.html', title='Page 1')
    return render_template('ex1.html', title='Page 1')

@application.route('/ex2')
def exercise2():
    if dark == True:
        return render_template('ex2.html', title='Page 2')
    return render_template('ex2.html', title='Page 2')