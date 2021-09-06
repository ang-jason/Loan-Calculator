from flask import Flask, render_template, flash, redirect,request, url_for,session
from app import application

from app.forms import InputParamForm
from werkzeug.exceptions import HTTPException




from app.loan_schedule_multiple import LoanScheduleMultiple
from app.loan_schedule import LoanSchedule

from app.analyse_schedule import AnalyseSchedule


# from app.static.library import grab_parameters


import numpy as np
import pandas as pd



@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    print("Generating index")
    form = InputParamForm()
    # if form.validate_on_submit():
    if request.method == 'POST' and form.validate():
        flash('Input requested for user {}, {},{}'.format(
            form.loan_amount.data, form.interest_rate.data, form.loan_tenor.data))
        print(form.loan_amount.data, form.interest_rate.data, form.term_periods.data, form.loan_tenor.data)
        print(type(form.loan_amount.data), type(form.interest_rate.data), type(form.term_periods.data), type(form.loan_tenor.data))
        
        # this statments store the values into the session using flask transparent to user
        
        session['T_LOANAMOUNT'] = form.loan_amount.data
        session['T_RATE'] = form.interest_rate.data
        session['T_TERM'] = form.term_periods.data
        session['T_TENOR'] = form.loan_tenor.data
        # print(session,type(session))
        return redirect(url_for('schedule'))
        # return redirect('/schedule')
        # redirect(url_for('schedule', T_LOANAMOUNT=request.form['loan_amount'],
                            # T_RATE=request.form['interest_rate'],
                            # T_TERM=request.form['term_periods'],
                            # T_TENOR=request.form['loan_tenor']))
        
        
    return render_template('index.html', title='Mortgage Calculator', form=form)

    # return render_template('index.html', title='Mortgage Calculator')
    
    
    

@application.route('/generate')
def generate():
    return render_template('generate.html', title='Loan Schedule')

@application.route('/about')
def about():
    return render_template('about.html', title='About')




# @application.route('/test', methods=['GET', 'POST'])
# def test():
    # form = InputParamForm()
    # if form.validate_on_submit():
        # flash('Input requested for user {}, {},{}'.format(
            # form.loan_amount.data, form.interest_rate.data, form.loan_tenor.data))
        # print(form.loan_amount.data, form.interest_rate.data, form.term_periods.data, form.loan_tenor.data)
        
        # return redirect('/test')
    # return render_template('/test_form.html', title='Sign In', form=form)


@application.route('/schedule', methods=['GET', 'POST'])
def schedule():
    print("in schedule")

    # For Testing
    # T_LOANAMOUNT=440248
    # T_RATE=[1.39,1.48,2.3]
    # T_TERM=[1,5,6]
    # T_TENOR=30
    # s1 = LoanSchedule(T_LOANAMOUNT,T_RATE,T_TENOR)
    # print(help(LoanSchedule))
    
    
    
    # this statments retrieve the values from the session using flask transparent to user
    T_LOANAMOUNT = session.get('T_LOANAMOUNT', None)
    T_RATE = session.get('T_RATE', None)
    T_TERM = session.get('T_TERM', None)
    T_TENOR = session.get('T_TENOR', None)

    # T_LOANAMOUNT=440248
    # T_RATE="1.39,1.48"
    # T_TERM="1,2"
    # T_TENOR=30
    print(type(T_LOANAMOUNT),type(T_RATE),type(T_TERM),type(T_TENOR))
    
    if "," in T_RATE or "," in T_TERM:

        lsm= LoanScheduleMultiple(T_LOANAMOUNT,T_RATE,T_TERM,T_TENOR)
        # # print(help(LoanScheduleMultiple))

    else:
        lsm= LoanSchedule(float(T_LOANAMOUNT),float(T_RATE),int(T_TENOR))
        # # print(help(LoanScheduleMultiple))

    # loan schedule in df
    x = lsm.show_schedule()
    # print("len",len(df),type(df))
    pd.options.display.float_format = '{:,.2f}'.format
    df_text="Your Loan Schedule" 
    df_desc="Loan Amount: "+ str(T_LOANAMOUNT)+ " Interest Rate(s): "+str(T_RATE)+ (" Terms: "+str(T_TERM) if T_TERM else "")+" Loan Tenor: "+str(T_TENOR)
    
    
    x = x.round(2)
    # print(x,type(x))  
    
    # put loan schedule x into AnalyseSchedule class for further summary generation
    summary=AnalyseSchedule(x)
    summary_dict=summary.loan_tabletop_brief()
    
    # AnalyseSchedule provide graphical analytics using chartjs by pulling each data sets
    yearly_labels,data_col_names,data_sbalance,data_payment,data_principal,data_interest=summary.show_yearly_brief()
    
    
    return render_template("schedule2.html",data=x,name=df_text,desc=df_desc,summary=summary_dict,
                                yearly_labels=yearly_labels,
                                data_col_names=data_col_names,
                                data_sbalance=data_sbalance,
                                data_payment=data_payment,
                                data_principal=data_principal,
                                data_interest=data_interest
                                )

    # return render_template('about.html', title='Mortgage Calculator') 




@application.errorhandler(404) 
def invalid_route(e): 
    return redirect('/')


@application.errorhandler(HTTPException)
def handle_exception(e): 
    return redirect('/')