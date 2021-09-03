

from app.LoanPackage import LoanPackage
from app.InterestRateMultiple import InterestRateMultiple
from app.TotalPeriod import TotalPeriod

# from LoanPackage import LoanPackage
# from InterestRateMultiple import InterestRateMultiple
# from TotalPeriod import TotalPeriod



class LoanPackagePayments(LoanPackage):
    def __init__(self,loan_amount,tenor,n_ir,n_term_end=[0]):
      super().__init__(tenor,n_ir,n_term_end)
      # self.loanpackage = LoanPackage(tenor,n_ir,n_term_end)
      self.loan_amount = loan_amount
       


    # property getter
    @property
    def loan_amount(self):
        return self._loan_amount
        
        
    # property setter
    @loan_amount.setter
    def loan_amount(self,value):
        print("loan amount setter")
        # if (isinstance(value, int) or isinstance(value, list))  and value != "":
        if value != "":
            self._loan_amount = float(value)



    # self._monthly_ir = InterestRateMarket(interest_rate_annual).compute_monthly 
    # this is helper function as various computation require this factor 
    def period_factor(self,rate,term_period):
        period_factor = (1+ rate)**(term_period)
        return float(period_factor)

      # this function returns monthly installments computed based on the loan
    def monthly_payment_computed(self,balance_amount,rate,term_period):
        monthly_payment = (balance_amount * rate) * self.period_factor(rate,term_period) / (self.period_factor(rate,term_period) - 1)
        print(round(monthly_payment,2))
        return monthly_payment

    def outstanding_amount(self,balance_amount,rate,term_period,period_paid):
        # Outstanding Loan Balance
        paid_period_factor = (1+ rate)**int(period_paid)
        outstanding_amount = (balance_amount * (self.period_factor(rate,term_period) - paid_period_factor)) / ( self.period_factor(rate,term_period) -1 )
        print(round(outstanding_amount,2))
        return outstanding_amount
        
        
        
    def compute_monthly_payments(self,starting_loan_amount):
        sbalance_amount, _term_period, _remaining_period = self.show_package_brief()
        rates_monthly_list = InterestRateMultiple(self.n_ir,self.n_term_end).given_monthly_rate_list
        rates_monthly_list=[x*100 for x in rates_monthly_list]
        print("rates_monthly_list",rates_monthly_list)
        monthly_install_list=[]
        for each in range(0,len(rates_monthly_list)):
            # print("DEBUG",rates_monthly_list[each],_remaining_period[each],_term_period[each])
            if each ==0 :
                monthly_payment = self.monthly_payment_computed(starting_loan_amount,rates_monthly_list[each],_remaining_period[each])
                sbalance_amount=self.outstanding_amount(starting_loan_amount,rates_monthly_list[each],_remaining_period[each],_term_period[each])
            else:
                if sbalance_amount >0:
                    monthly_payment = self.monthly_payment_computed(sbalance_amount,rates_monthly_list[each],_remaining_period[each])
                    sbalance_amount=self.outstanding_amount(sbalance_amount,rates_monthly_list[each],_remaining_period[each],_term_period[each])
            monthly_install_list.append(monthly_payment)
            # print(each)
        return monthly_install_list
        
        
    # this function return an array length of total period of installments
    def installments_array(self):
        # print(self.monthly_payment())
        monthly_install_list=self.compute_monthly_payments(self.loan_amount)
        monthly_install_arr = self.generate_ix_table(monthly_install_list)
        # print(monthly_install_arr,type(monthly_install_arr))
        return monthly_install_arr





    # this function returns monthly installments computed based on the loan + TOP UPS!
    # default assume 0 top up
    def monthly_payments(self,other=0):
        monthly_topup_arr = [other] * self.totalperiod.total_period
        monthly_installs_arr = self.installments_array()
        # monthly_payments_arr = self.installments_array() + monthly_topup_arr
        monthly_payments_arr = [ monthly_installs_arr[x] + monthly_topup_arr[x] for x in range (len(monthly_installs_arr))]  
        return monthly_payments_arr




    def show_package_brief(self):
        answer = self.generate_ix_table(self.n_ir)
        from collections import Counter
        rates_list=Counter(answer).keys()
        term_list=Counter(answer).values()
        # print(type(rates_list),type(term_list))
        # print(Counter(answer))
        # print(len(Counter(answer)))
        
        # print(self.totalperiod)
        remainder=[self.totalperiod.total_period]
        for each in list(term_list):
            remainder.append(remainder[-1]-each)
        
        # drop last element
        remainder.pop()
        return list(rates_list),list(term_list),remainder
        # return list(rates_list),list(term_list)



# # ### FOR TESTING
# print("============================================== LoanPackagePayments =======================")
# loan_amount=440248
# ir_package1=[1.39,1.48,2.3]
# testerA=LoanPackagePayments(loan_amount,30,ir_package1)

# testerA.n_term_end=[1,5,6]
# # print(testerA)
# print("testerA.n_ir",testerA.n_ir,type(testerA.n_ir))
# print("testerA.n_term_end",testerA.n_term_end,type(testerA.n_term_end))
# print("============================================== LoanPackagePayments =======================")
# # print(help(testerA))

# brief_rate, brief_length,brief_remaining=testerA.show_package_brief()

# print(brief_rate, brief_length,brief_remaining)
# print(type(brief_rate), type(brief_length),type(brief_remaining))


# testerA.monthly_payment_computed(440248,1.39/100/12,360) ##1496.26

# outstand = testerA.outstanding_amount(440248,1.39/100/12,360,12) ## 428336.68
# testerA.monthly_payment_computed(outstand,1.48/100/12,360-12) ## 1514.58

# outstand = testerA.outstanding_amount(outstand,1.48/100/12,360-12,48) ## 379596.03



# answer=testerA.compute_monthly_payments()
# print(answer)



# arr = testerA.installments_array()
# print(len(arr))