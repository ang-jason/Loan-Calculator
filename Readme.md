[![PayPal donate button](https://img.shields.io/badge/Support-LoanCalculator-blue)](https://github.com/ang-jason/Loan-Calculator)
# Loan Calculator
Loan Calculator is a app-lite Python library providing analytics and amortisation table for your mortgage computation (local context)

### This is an open-ended category.

##### Quick Calculator Software: You may tend to do some specific calculation again and again. As an example, it can be your financial calculator for investment or retirement savings. You can write a Python program to do these tasks.


## Motivation*
- Everyone in Singapore will want to attain a house. Be it public and private housing, the needful of taking a loan will be a necessity
- You should be able to make an informed decision for your loan/mortgage (a real live example)
- Understand the mechanics behind them
- How interest rate affects the mortgage
- Demystify public domain lingo and what it entails

<img src="https://github.com/ang-jason/Loan-Calculator/blob/main/misc_docs/Capture3.PNG?raw=true" width="50%" height="50%"><img src="https://github.com/ang-jason/Loan-Calculator/blob/main/misc_docs/Capture4.PNG?raw=true" width="50%" height="50%"><img src="https://github.com/ang-jason/Loan-Calculator/blob/main/misc_docs/Capture2.PNG?raw=true" width="50%" height="50%">


## Introduction*
A mortgage entails paying your monthly payments (installments). The party that provides the loan can be a financial institution (ie. the Bank)
To compute the monthly payments - it is a function (loan amount, interest rates, loan duration)
<img src="https://i.imgur.com/YX9Gw1R.png" width="70%" height="70%">
(picture from https://www.wallstreetmojo.com/mortgage-formula/)

- **P** - Princpal, Loan amount `$440,248`
- **r** - Annual interest rate `1.39%pa`
- **n** - Number of payable periods (typical in months) (`30` years)

For a fixed interest rate (`1.39%`), the monthly payment will be fixed throughout the loan. If it is a variable rate, then your monthly payment will be recomputed every fixed date by the policy of the loan. In market convention, the rate is quoted in an annual basis, and since the payment period is in monthly terms, the monthly rate will be the annual rate is divided by 12. (ie `1.39%/12`)


Every month, the payment (`$1,496.26`) to the bank does not directly attribute to your outstanding loan.
A monthly payment consists of two components - Principal, **P** and Interest, **I**

Bank will like to take their benefit of providing you the loan - it is the interest. Computed by the previously agreed rate (ie. `1.39%/12`) of the outstanding loan. (`$509.95`)

The remaining amount will be used to pay your outstanding loan. (ie. Principal `$986.30`)

Your loan amount will left `$440,248 - $986.30 = $439,261.70`

This happens in Month 1 of your loan. The following month, you pay the same payment of `$1,496.26` to the bank. 

Bank will take their benefits, the interest `$508.81` which is recomputed based on the outstanding loan balance `$439,261.70` using the same interest rate.

The principal amount ` $987.44` will be used to pay your outstanding loan. 

The outstanding loan balance will reduce to `$438,274.25`.

This will continue for the entire duration of the loan `30` years of `12*30=360` payments. The above setup the payment schedule or amortization  table for this web app.

If it is package terms (`1.39%`, `1.48%`, `2.3%`) or variable rates, the interest rate and its periods will differ, resulting in the monthly payments changing accordingly.


## Setup (on Linux)
1. Clone the repository from Github. On your terminal or Git Bash
2. Create Virtual Environment (MacOS/Linux): From the root folder, i.e. `Loan-Calculator`, create virtual environment called `virtenv`.
3. A folder called `virtenv` will be created. Now, activate the virtual environment.
4. Install the necessary packages for this library
5. Run flask to spin up the setup
```
git clone https://github.com/ang-jason/Loan-Calculator
cd Loan-Calculator
python -m venv virtenv
source virtenv/bin/activate
pip install -r requirements.txt
flask run
```

#### Dev Environment or Vocareum
The following will be displayed on screen:
```
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Once it is running, you can open another tab in your browser and type the following url: https://myserver.vocareum.com/.

To stop the web app type `CTRL+C`.

If you are using your own computer, make sure to change the flag voc=False in the following line inside `/app/__init__.py`.
```
# set voc=False if you run on local computer
application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=False)
```
[Setting up issues here](#Vocareum-Troubleshooting)
## Flask Website Usage
**1. Upon accessing the website, input the parameters of the loan.**

###### Example of a typcial loan offering:

>3.39%pa for period Year 0 and up to Year 1. 
>4.48%pa for period up to Year 5 (Year 2 - Year 5)
>5.30%pa for period from Year 6 onwards (Year 5 - Year 6 onwards)

Loan amount `440248`
Annual interest rate `1.39,1.48,2.3`
Term Periods `1,5,6`
Loan Tenor `30`

###### *When there is single(fixed) interest rate, term period will be ignored. Different interest rate as well as Term periods are separated by single commas (no spaces), no need for decimals-denomination and percentage.*

![Loan Calculator](https://github.com/ang-jason/Loan-Calculator/blob/main/misc_docs/frontpage1.PNG?raw=true)

**2. Click Show Schedule**

![Loan Calculator](https://github.com/ang-jason/Loan-Calculator/blob/main/misc_docs/frontpage2.PNG?raw=true)


## Code Usage
The design of this library orginated from a single interest rate throughout the loan tenor and expanding further with features of different interest rates of associated loan periods. Output schedule is using pandas dataframe suitable for time series manipulation.

*Computation were generally done with minimum rounding. Recouncilation were performed to rounding of monthly payment as it illustrate billing to your two decimal places and the diference were negligence.*

### Initiation of Loan Schedule

```python
# Begin by importing the LoanSchedule class
# for single interest rate(fixed)
from loan_schedule import LoanSchedule

# Create a simple loan
# THE_LOANAMOUNT=440248
# THE_RATE=1.39
# THE_TENOR=30

# initialse the instance of LoanSchedule
fixed_rate = LoanSchedule(THE_LOANAMOUNT, THE_RATE, THE_TENOR)

# returns of loan schedule table of dataframe
# with headers 'StartBalance','Payment', 'Principal', 'Interest', 'EndBalance'
fixed_rate.show_schedule()

# returns info on the monthly installments of the loan ($1,496.26)
fixed_rate.monthly_payment_computed()


# for 'package type' interest rates & period terms
# distinction: this module is meant for multiple rates & terms
from loan_schedule_multiple import LoanScheduleMultiple

# typical package: 1.39%pa for period up to Year 1.
#                  1.48%pa for period up to Year 5 (Year 2 - Year 5)
#                  2.30%pa for period from Year 6 onwards (Year 5 - Year 6 onwards)
#                  
# THE_LOANAMOUNT=440248
# THE_RATE=[1.39,1.48,2.3]
# THE_TERM=[1,5,6]
# THE_TENOR=30


# initialse the instance of LoanScheduleMultiple
package_rate = LoanScheduleMultiple(THE_LOANAMOUNT, THE_RATE, THE_TERM, THE_TENOR)

# returns of loan schedule table of dataframe
# with headers 'StartBalance','Payment', 'Principal', 'Interest', 'EndBalance'
package_rate.show_schedule()

```

### Processing analytics
After generating the `show_schedule()` dataframe, we make use of `AnalyseSchedule` module to provide further analytics.

```python
# importing the class definition
from analyse_schedule import AnalyseSchedule

# loan schedule x into AnalyseSchedule class for further summary generation
summary = AnalyseSchedule(x)

# this function is for the summary of the loan
# returns total payments, principal, interest of the entire loan
total_payment, total_principal, total_interest = summary.total_ppi()

# this function is analysis of how much interst vs the principal amount
# returns ratio in percentage
ratio = summary.interest_to_principal()

# this function is analysis of how much payment vs the loan amount
# returns ratio in percentage
ratio = summary.payment_to_loan()

# this function is to return specific row (period_row) of the dataframe's schedule
# input based on months less 1 due to starting 0.
# e.g Year 2 = 2*12 = 24 -1 = 23th row
year2_row = summary.show_schedule_row(2*12-1)

# this function to return the quick view of monthly payment and the number of times the payments to be made
mthly_payments, mthly_period = summary.show_payments_brief()


# this function is to analytical table top summary of the loan
# returns the format should be as shown below (dictionary type)
# Your Table Top Summary of the Loan
# Total interest payable: XXX
# Total principal: XXX
# Total payable: XXX
#
# Total payments to loan ratio: XXX
# Associated monthly payments: XXX
#
# Principal Balance after Year 2: XXX
# Principal Balance after Year 3: XXX
# Principal Balance after Year 5: XXX
quick_summary = summary.loan_tabletop_brief()

# to return individual colums of list of yearly rows to pipe into chartjs
# provide graphical analytics using chartjs by pulling each data columns set
yearly_labels, data_col_names, data_sbalance, data_payment, \
 data_principal, data_interest = summary.show_yearly_brief()

```

## UML Diagram
#### Main Web App 
![Loan Calculator UML Diagram](https://github.com/ang-jason/Loan-Calculator/blob/main/misc_docs/uml_diagram1.PNG?raw=true)

#### Analytical Module
![Loan Calculator UML Diagram](https://github.com/ang-jason/Loan-Calculator/blob/main/misc_docs/uml_diagram2.PNG?raw=true)


## Under the hood
InterestRateMarket class was created with future flexible of market conventions. Some financial institution may differ from market convention.

*E.g if the interest rate is 1.39% pa. The monthly rate will be 1.39%/12(months).*

There is a possible that the computation could be divided by 360/365 (days) and multiple by calendar days in month or 30.

```python    
class InterestRateMarket:
    def __init__(self, given_annual_rate, year_length=12, month_length=0):
        self.given_annual_rate = given_annual_rate/100.0
        self.year_length = year_length
        self.month_length = month_length

```
Expanding on to the various available loan packages in the market, InterestRateMultiple class was created to accept multiple stepped interest rates and term periods.

```python    
class InterestRateMultiple(InterestRateMarket):
    def __init__(self, given_annual_rate_list, given_term_period_list):
        self.given_annual_rate_list = given_annual_rate_list
        self.given_term_period_list = given_term_period_list
        self.given_monthly_rate_list = given_annual_rate_list

```


## Future Features or Improvements
- [ ] improve UI
- [ ] consideration of js implementation
- [ ] resolve corner cases
- [ ] add accordion for yearly row


## Notes
Reconciliation working excel file provided in `misc_docs`.

Code were written and clean up to PEP8 guide (using https://github.com/PyCQA/pycodestyle).

## References
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
https://stackoverflow.com/questions/14652325/python-dictionary-in-to-html-table/14656262
https://stackoverflow.com/questions/7975365/how-can-i-make-this-loop-with-jinja2
https://github.com/abulka/pynsource
https://www.moneysense.gov.sg/financial-tools/mortgage-calculator


## Vocareum Troubleshooting
```
You are using pip version 10.0.1, however version 21.2.4 is available.       
You should consider upgrading via the 'pip install --upgrade pip' command. 
```
Consider updating pip first before `pip install -r requirements.txt`

`pip install --upgrade pip`


#### Hyperlink within pages should be adjusted
```html    
<!-- use this instead of -->
href='index'
<!-- this (due to Vocareum) -->
href='/index'
```