from app.loan import Loan
from app.interest_rate_market import InterestRateMarket
from app.total_period import TotalPeriod


# from loan import Loan
# from interest_rate_market import InterestRateMarket
# from total_period import TotalPeriod

import numpy as np
import pandas as pd
# Class definition
class LoanSchedule(Loan):
    '''
    This is LoanSchedule Class that take compute the payment schedule and show the amorization table using the other needed parameters

    Expanding for the default Loan Class to compute and present the payment schedule
    
    The basic principle is of working out the payment schedule/ amorization table is first computed the monthly installments (using monthly rates derived from pa interest rate, loan length in months and final value theory)
    
    Monthly installments conprises of Principal (P) + Interest (I). (constant for the period you have computed)
    
    Interest portion is computed based on the monthly interest rate on the balance of the loan (starting balance of loan in each period) each payment period (ie 1 of 360 period).
    
    With the interest, taking monthly installment less interest will be the principal. Using this principal, this will reduce your loan balance. (equate to Ending Balance)

    The next payment period, a new interest portion will be computed using the new balance (ie starting balance) from the pervious ending balance.
    
    Then, principal will be reduce by lessing interest portion from the installments. Following reduce the balance with the new principal final with ending balance.
    
    The whole cycle completes until the end of the loan period (loan tenor, after 360 payments)

    show_schedule() will present as compute_schedule() will compute the above with helper functions like monthly payments, principal_function, interest_function.
    
    items were built in an array form, representing column and reduce row by row to form the table using the above concept.
    
    show_schedule will return a pandas dataframe and using the internal variables provided from the intial loan_amount, interest_rate_annual, tenor
    This class also makes class instances of InterestRateMarket and TotalPeriod
    Using of pandas dataframe allows one to manipulate the schedule data easily for further analysis.
    
    **avenue for expansion was inbuilt partially to cater top up to the loan- which later reduced in priority over other features. 

    '''
    # Attributes:
    def __init__(self,loan_amount, interest_rate_annual, tenor, topup_amount=0,format=0):
        super().__init__(loan_amount, interest_rate_annual, tenor)
        self._monthly_ir = InterestRateMarket(interest_rate_annual).compute_monthly
        self._total_period = TotalPeriod(tenor).total_period
        self._topup_amount = topup_amount
        # pass
        # super().__init__(self)


    # property getter
    @property
    def topup_amount(self):
        return self._topup_amount



    # property getter
    @property
    def total_period(self):
        # print(self._total_period)
        return self._total_period

    # property getter
    @property
    def monthly_rate(self):
        # print(self._monthly_ir)
        return self._monthly_ir

    # this is helper function as various computation require this factor 
    def period_factor(self):
        period_factor = (1+ self._monthly_ir)**(self._total_period)
        return float(period_factor)


    # this function returns monthly installments computed based on the loan
    def monthly_payment_computed(self):
        # print((1+ self._monthly_ir))
        # self.period_factor = (1+ self._monthly_ir)**(self._total_period)
        # print(self.period_factor())
        monthly_payment = (self.loan_amount * self._monthly_ir) * self.period_factor() / (self.period_factor() - 1)
        print(round(monthly_payment,2))
        return monthly_payment


    # this function return an array length of total period of installments
    def installments_array(self):
        # print(self.monthly_payment())
        monthly_install_arr = [self.monthly_payment_computed()] * self._total_period
        # print(monthly_install_arr,type(monthly_install_arr))
        return monthly_install_arr

    # this function returns monthly installments computed based on the loan + TOP UPS!
    # default assume 0 top up
    def monthly_payments(self,other=0):
        monthly_topup_arr = [other] * self._total_period
        monthly_installs_arr = self.installments_array()
        # monthly_payments_arr = self.installments_array() + monthly_topup_arr
        monthly_payments_arr = [ monthly_installs_arr[x] + monthly_topup_arr[x] for x in range (len(monthly_installs_arr))]  
        return monthly_payments_arr


    def __str__(self):
        return f"Monthly rate: {self._monthly_ir*100:.10f}, Total Period: {self._total_period}"

    def principal_function(self,begining_amount):
        principal_n = monthly_payment - interest_n
        return principal_n

    def interest_function(self,begining_amount):
        interest_n = begining_amount * self._monthly_ir
        return interest_n

    def outstanding_amount(self,period_paid):
        # Outstanding Loan Balance
        paid_period_factor = (1+ self._monthly_ir)**int(period_paid)
        outstanding_amount = (self.loan_amount * (self.period_factor() - paid_period_factor)) / ( self.period_factor() -1 )
        return outstanding_amount


    def compute_schedule(self):
        print("(DEBUG) computing single Schedule")
        nth = range(0, self._total_period)
        # nth=range(0,5)
        # print(nth,len(nth))
        result_b_start=[]
        result_b_end=[]
        resultp=[]
        resulti=[]
        payments=self.monthly_payments()
        # print("len(payments)",len(payments))
        for each in nth:
            # print(self.interest_function(payments[each]))
            # print(each,self.loan_amount)
            if each == 0:
                result_b_start.append(self.loan_amount)
                
                # compute new payments if there is.
                resulti.append(self.interest_function(result_b_start[-1]))
                resultp.append(payments[each]-resulti[-1])
                result_b_end.append(result_b_start[-1]-resultp[-1])
            else:
                result_b_start.append(result_b_end[-1])
                
                # compute new payments if there is.
                resulti.append(self.interest_function(result_b_start[-1]))
                resultp.append(payments[each]-resulti[-1])
                result_b_end.append(result_b_start[-1]-resultp[-1])

        return result_b_start,payments,resultp,resulti,result_b_end            
            # else:
            #     print(each)
            # print(resultb)
        # return self.resultb


    ## to display schedule
    def show_schedule(self):
        result_b_start,payments,resultp,resulti,result_b_end=self.compute_schedule()
        print("Display Schedule...")
        table_labels=[result_b_start,payments,resultp,resulti,result_b_end]
        # for label in table_labels:
            # print(len(label))


        ## convert all the list to dataframe for presentation
        df = pd.DataFrame(table_labels)
        # print(df)

        ## Transpose the df
        df=df.T
        df=df.round(4)

        ## data frame labels
        df.columns = ['StartBalance','Payment', 'Principal', 'Interest', 'EndBalance']
        df.index += 1 
        # with pd.option_context('display.max_colwidth', None):
          ## display(df)
          # print(df.head(13))
          # print(df.tail(13))
        print("printed to html")
        df.to_html('./app/templates/generate.html')
        return df











# # For Testing
# T_LOANAMOUNT=440248
# T_RATE=1.39
# T_TENOR=30
# s1 = LoanSchedule(T_LOANAMOUNT,T_RATE,T_TENOR)
# # print(help(LoanSchedule))


# result_b_start,payments,resultp,resulti,result_b_end=s1.compute_schedule()

# table_labels=[result_b_start,payments,resultp,resulti,result_b_end]
# # for each_x in x:
# #     print(s1.outstanding_amount(each_x))
# for label in table_labels:
    # print(len(label))

# import pandas as pd

# ## convert all the list to dataframe for presentation
# df = pd.DataFrame(table_labels)
# print(df)

# ## Transpose the df
# df=df.T
# df=df.round(4)

# ## data frame labels
# df.columns = ['SBalance','Payments', 'Principal', 'Interest', 'EBalance']
# df.index += 1 
# with pd.option_context('display.max_colwidth', None):
  # # display(df)
  # print(df.head(13))
  # print(df.tail(13))