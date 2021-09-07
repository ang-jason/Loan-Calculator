# from loan_schedule import LoanSchedule
# from loan_package_payments import LoanPackagePayments
# from interest_rate_multiple import InterestRateMultiple
# from total_period import TotalPeriod


from app.loan_schedule import LoanSchedule
from app.loan_package_payments import LoanPackagePayments
from app.interest_rate_multiple import InterestRateMultiple
from app.total_period import TotalPeriod


# Class definition
class LoanScheduleMultiple(LoanPackagePayments, LoanSchedule):
    '''
    Extedning from the LoanPackagePayments Class and
    making use for the certain function in LoanSchedule Class.
    This class allow list of interest rates and
    term period as described detailedly in InterestRateMultiple class
    Further description were illustrated in LoanSchedule class.
    As the input parameters of interest rate and
    their associated term period were provided in a list format.
    This class further worked on the LoanPackagePayments
    class to finally compute the loan schedule table
    using various components classes that was created earlier.
    The instantiation of helper classes for some computation
    - a design choice from the getgo so as to quickly access
    derived figures for further computation instead of digging
    into the nested classes and unroll and parent up again.
    (e.g InterestRateMultiple,TotalPeriod)
    Functions overwrite were done for compute_schedule()
    in this class of different sets of interests rates,
    payments, term periods and durations.
    Lastly, as the presentation component were built in
    LoanSchedule class, this function componet were
    called to use to prevent rewriting. mechanics of
    the show_schedule() is illustrated in the LoanSchedule class.
    '''
    def __init__(self, loan_amount, interest_rate_annual_list, tenor_list, tenor):
        # https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
        # https://stackoverflow.com/questions/222877/what-does-super-do-in-python-difference-between-super-init-and-expl
        # LoanPackagePayments.__init__(self,tenor,interest_rate_annual_list,tenor_list)
        super().__init__(loan_amount, tenor, interest_rate_annual_list, tenor_list)
        self._ir_obj = InterestRateMultiple(interest_rate_annual_list, tenor_list)
        self._total_period = TotalPeriod(tenor).total_period

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
        print("(DEBUG) computing with new Mutiple Schedule")
        nth = range(0, self._total_period)
        # nth=range(0,5)
        # print(nth,len(nth))
        result_b_start = []
        result_b_end = []
        resultp = []
        resulti = []
        payments = self.installments_array()
        interest_arr = self.interst_function()
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

        return result_b_start, payments, resultp, resulti, result_b_end
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