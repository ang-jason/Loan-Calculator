
import pandas as pd


# Class definition
class AnalyseSchedule():
    '''
    This AnalyseSchedule Class is to perform table top analytics on the schedule (dataframe)
  
    A Basic getter and setter functions to parameters and the intended data types (dataframe)

    '''
    # Attributes:
    def __init__(self,df):
        self.df = df

    # property getter
    @property
    def df(self):
        return self._df
    
    # property setter
    @df.setter
    def df(self, df_value):
        if isinstance(df_value, pd.DataFrame) and not df_value.empty:
            self._df = df_value
    ''' 
    this function is for the summary of the loan
    
    returns total payments, principal, interest of the entire loan

    '''
    def total_ppi(self):
        total_payment=sum(self._df['Payment'])
        total_principal=sum(self._df['Principal'])
        total_interest=sum(self._df['Interest'])
        
        return total_payment,total_principal,total_interest

    # this function is analysis of how much interst vs the principal amount returns ratio in percentage
    def interest_to_principal(self):

        total_payment,total_principal,total_interest=self.total_ppi()
        ratio=total_interest/total_principal*100
        return ratio

    # this function is analysis of how much payment vs the loan amount returns ratio in percentage
    def payment_to_loan(self):

        total_payment,total_principal,total_interest=self.total_ppi()
        loan_size=self._df['StartBalance'].iloc[0]
        
        ratio=total_payment/loan_size*100
        return ratio

    # this function is to return specific row (period_row) of the dataframe's schedule
    def show_schedule_row(self,period_row):

        return self._df['StartBalance'].iloc[period_row], \
                    self._df['Payment'].iloc[period_row],    \
                    self._df['Principal'].iloc[period_row],  \
                    self._df['Interest'].iloc[period_row],   \
                    self._df['EndBalance'].iloc[period_row]
                    
    # this function to return the quick view of monthly payment and the number of times the payments to be made
    def show_payments_brief(self):
        answer = self._df['Payment']
        from collections import Counter
    
        return Counter(answer).keys(),Counter(answer).values()
        
    # this function to return individual colums of list to pipe into chartjs 
    def show_yearly_brief(self):
        yearly=len(self._df)//12
        data_sbalance=[]
        data_payment=[]
        data_principal=[]
        data_interest=[]
        for i in range(yearly):
            # print(self.show_schedule_row(i*12))
            #capture starting balance, payments and principal, interest? more meaning?
            data_sbalance.append(self.show_schedule_row(i*12)[0])
            data_payment.append(self.show_schedule_row(i*12)[1])
            data_principal.append(self.show_schedule_row(i*12)[2])
            data_interest.append(self.show_schedule_row(i*12)[3])  
            
        yearly_labels=[ x+1 for x in range(yearly)]
        # print(yearly_labels)
        data_col_names = [self._df.columns[x] for x in range(len(self._df.columns)) if x < 4]
        # print(data_col_names)
        return yearly_labels,data_col_names,data_sbalance,data_payment,data_principal,data_interest
        
    ''' 
    this function is to analytical table top summary of the loan
    (this basic format should be as shown below)
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
    '''    
    def loan_tabletop_brief(self):

        # this is for total_payment,total_principal,total_interest
        total_payment,total_principal,total_interest=self.total_ppi()

        # this is for payment to loan ratio
        ratio=self.payment_to_loan()

        # this is for assoicated monthly payments
        mthly_payments,mthly_period=self.show_payments_brief()
        mthly_payments=['$ {0:.{1}f}'.format(x, 2) for x in mthly_payments]
        # print("This is year 2 loan period")
        # print("This is year 3 loan period")
        # print("This is year 5 loan period")
        byear2,byear3,byear5=self.show_schedule_row(2*12-1),    \
                                self.show_schedule_row(3*12-1), \
                                self.show_schedule_row(5*12-1)

        # pd.options.display.float_format = '{:,.2f}'.format
        resultant={
            "Total interest payable": f'$ {total_interest:.0f}',
            "Total principal": f'$ {total_principal:.0f}',
            "Total payable": f'$ {total_payment:.0f}',
            "Total payments to loan ratio":f'{ratio:.1f} %',
            "Associated monthly payments": ' '.join(mthly_payments),
            "Principal after Year 2": f'$ {byear2[-1]:.0f}',
            "Principal after Year 3": f'$ {byear3[-1]:.0f}',
            "Principal after Year 5": f'$ {byear5[-1]:.0f}',
            }
       
        return resultant
        
    def __str__(self):
        print(f"-"*50)
        display_txt="This is your schedule: \n"
        print(f"-"*50)
        display_txt+=f"${self._df}"
        return display_txt
        
        



    