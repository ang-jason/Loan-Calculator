from flask import render_template
from app import application




@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html', title='Mortgage Calculator')

@application.route('/generate')
def generate():
    return render_template('write_html.html', title='Loan Schedule')

@application.route('/about')
def about():
    return render_template('about.html', title='About')

@application.route('/schedule/')
def schedule():

    import pandas as pd
    import random
    import numpy as np
    x = pd.DataFrame(np.random.randn(20, 5))
    x = x.round(2)
    
    return render_template("schedule.html",name="TESTING TABLE" ,data=x)
    # return render_template("schedule.html",name="TESTING TABLE" ,data="write_html.html")

# @application.route('/ex2')
# def exercise2():
    # return render_template('ex2.html', title='Mini Project 1 Exercise 2')
    