# from LoanSchedule import LoanSchedule

# from LoanPackagePayments import LoanPackagePayments

# from InterestRateMultiple import InterestRateMultiple
# from TotalPeriod import TotalPeriod

from app.LoanSchedule import LoanSchedule

from app.LoanPackagePayments import LoanPackagePayments

from app.InterestRateMultiple import InterestRateMultiple
from app.TotalPeriod import TotalPeriod




# Class definition
class LoanScheduleMultiple(LoanPackagePayments,LoanSchedule):
    def __init__(self,loan_amount, interest_rate_annual_list, tenor_list,tenor):
    
    # https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
    # https://stackoverflow.com/questions/222877/what-does-super-do-in-python-difference-between-super-init-and-expl
    
        # LoanPackagePayments.__init__(self,tenor,interest_rate_annual_list,tenor_list)
        super().__init__(loan_amount,tenor,interest_rate_annual_list,tenor_list)

        self._ir_obj = InterestRateMultiple(interest_rate_annual_list,tenor_list)
        self._total_period=TotalPeriod(tenor).total_period
        
        
    # def compute_monthly_payments(self):
        # LoanPackagePayments.compute_monthly_payments(self)
    # def installments_array(self):
        # LoanPackagePayments.installments_array(self)
    # def monthly_payment_computed(self):
        # LoanPackagePayments.monthly_payment_computed()
        

    
    def interst_function(self):
        # print(len(self._ir_obj.given_monthly_rate_list),self._ir_obj.given_monthly_rate_list)
        # return self._ir_obj.given_monthly_rate_list
        interest_arr = self.generate_ix_table(self._ir_obj.given_monthly_rate_list)
        return interest_arr




    def compute_schedule(self):
        print("(DEBUG) using new Mutiple Schedule")
        nth = range(0, self._total_period)
        # nth=range(0,5)
        print(nth,len(nth))
        result_b_start=[]
        result_b_end=[]
        resultp=[]
        resulti=[]
        payments=self.installments_array()
        interest_arr=self.interst_function()
        # print("payments",payments)
        # print("len(payments)",len(payments))
        for each in nth:
            # print(self.interest_function(payments[each]))
            # print(each,self.loan_amount)
            if each == 0:
                result_b_start.append(self.loan_amount)
                
                # compute new payments if there is.
                resulti.append((result_b_start[-1])*interest_arr[each])
                resultp.append(payments[each]-resulti[-1])
                result_b_end.append(result_b_start[-1]-resultp[-1])
            else:
                result_b_start.append(result_b_end[-1])
                
                # compute new payments if there is.
                resulti.append(result_b_start[-1]*interest_arr[each])
                resultp.append(payments[each]-resulti[-1])
                result_b_end.append(result_b_start[-1]-resultp[-1])

        return result_b_start,payments,resultp,resulti,result_b_end            
        


        
            # else:
            #     print(each)
            # print(resultb)
        # return self.resultb
        
# # For Testing
# T_LOANAMOUNT=440248
# T_RATE=[1.39,1.48,2.3]
# T_TERM=[1,5,6]
# T_TENOR=30

# lsm= LoanScheduleMultiple(T_LOANAMOUNT,T_RATE,T_TERM,T_TENOR)
# lsm.show_package_brief()

# answer=lsm.compute_monthly_payments()
# # print(answer)

# # print(lsm)
# # ans=lsm.interst_function()
# # print(len(ans),ans)
# print("=======================================")
# # lsm.compute_schedule()
# df=lsm.show_schedule()

# import pandas as pd
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    # print(df)
  # # print(df.head(13))
  # # print(df.tail(13))
# # df.to_html('write_html.html', justify='center')
# # print(tester)



# # # For Testing
# T_LOANAMOUNT=440248
# T_RATE="1.39,1.48,2.3"
# T_TERM="1,5,6"
# T_TENOR=30

# lsm= LoanScheduleMultiple(T_LOANAMOUNT,T_RATE,T_TERM,T_TENOR)
# lsm.show_package_brief()

# answer=lsm.compute_monthly_payments(T_LOANAMOUNT)
# print("answer",answer)

# print(lsm)
# ans=lsm.interst_function()
# print(len(ans))
# print("=======================================")
# lsm.compute_schedule()
# df=lsm.show_schedule()

# import pandas as pd
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    # print(df)




# For Testing
# T_LOANAMOUNT=440248
# T_RATE="1.39,1.48"
# T_TERM="1,2"
# T_TENOR=30

# lsm= LoanScheduleMultiple(T_LOANAMOUNT,T_RATE,T_TERM,T_TENOR)
# lsm.show_package_brief()

# answer=lsm.compute_monthly_payments(T_LOANAMOUNT)
# print("answer",answer)

# print(lsm)
# ans=lsm.interst_function()
# print(len(ans))
# print("=======================================")
# lsm.compute_schedule()
# df=lsm.show_schedule()

# import pandas as pd
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    # print(df)