
# from total_period import TotalPeriod
# from tnterest_rate_multiple import InterestRateMultiple

from app.total_period import TotalPeriod
from app.interest_rate_multiple import InterestRateMultiple

class LoanPackage():
    '''
    Expanding for the default Loan Class which allows only single interest rate
    
    This class allow list of interest rates and term period as described detailedly in InterestRateMultiple class
    
    Key element is the generate_ix_table which allow usage of setting up arrays of respective interest rates and associated periods.
    e.g. IR=1.35,1.5,1.8
        Term=2,3,4
        
    [1.35 --- x12 (for year1), 1.35 x12 (for year 2), 1.5,1.5.. x12 (for year 3), 1.8 ... x12 for (year4), 1.8... end of the total period]
        
    Tenor input is to govern the total length ie 30 years will have 30*12=360 associated interest rates which first 12 will be 1.35, next 12 will be 1.35 and 1.5 following 12 and 1.8 for year4's 12 and until the end of loan length
    
    
    A Basic getter functions to get inputted parameters. Input values were governed by InterestRateMultiple and TotalPeriod as there were class instances in them.
    '''

    def __init__(self,tenor,n_ir,n_term_end=[0]):
        # self.n_ir = n_ir
        # self.n_term_end = n_term_end
        self.loanpackage = InterestRateMultiple(n_ir, n_term_end)
        self.totalperiod = TotalPeriod(tenor)



    # property getter
    @property
    def n_ir(self):
        return self.loanpackage.given_annual_rate_list
    # property getter
    @property
    def n_term_end(self):
        return self.loanpackage.given_term_period_list
        
        
    # # property setter
    # @n_ir.setter
    # def n_ir(self,value):
        # # if isinstance(value, str):
            # # print("input is string")
        # # if (isinstance(value, float) or isinstance(value, list))  and value != "":
        # if value != "":
            # self._n_ir = value

    # # property getter
    # @property
    # def n_term_end(self):
        # # print("(DEBUG)",self._n_term_end)
        # return self._n_term_end

    # property setter
    @n_term_end.setter
    def n_term_end(self,value):
        # if (isinstance(value, int) or isinstance(value, list))  and value != "":
        if value != "":
            self.loanpackage.given_term_period_list = value


    # def generate_ir_table(self):
    #     total_ir_table = [0] * self.totalperiod.total_period
    #     total_ir_table = [0] * 10
    #     for each in range(0,len(total_ir_table)):
    #         print(each)
    #         if self._n_term_end !="":
    #             print("LEN",len(self._n_term_end))
    #             if len(self._n_term_end)>0 and each <= self._n_term_end[0]:
    #                 # print(each)
    #                 # total_ir_table[each]="X"
    #                 total_ir_table[each]=self._n_ir[each]
    #                 print(total_ir_table)                
    #                 if each == self._n_term_end[0]:
    #                     self._n_term_end.pop(0)
    #                     print(self._n_term_end)
                
    #     return total_ir_table

    def generate_ix_table(self,n_table):
            
        # print("n_table",n_table,type(n_table))    
        # print("self.n_term_end",self.n_term_end,type(self.n_term_end))
        if isinstance(self.n_term_end, float):
            self.n_term_end=[0]
            # self.n_term_end.append(int(0))
            # print("self.n_term_end",self.n_term_end,type(self.n_term_end))

        ir_table=[]
        for each in range(0,len(n_table)):
            # print(each)
            # print(n_table[each],self._n_term_end[each])
            if each == 0:
                ir_table.append([n_table[each]]*(self.n_term_end[each])*12)
            else:
                ir_table.append([n_table[each]]*((self.n_term_end[each]-each)*12))

        # print(ir_table)

        ## for debug
        # for each_row in ir_table:
        #     print("row",len(each_row))


        flat_list = [item for sublist in ir_table for item in sublist]
        
        # print(len(flat_list),self.totalperiod.total_period-len(flat_list))

        for each_again in range(len(flat_list),self.totalperiod.total_period):
            flat_list.append(n_table[each])
        # print(flat_list)
        return flat_list

    def __str__(self):
        # return f"{self.totalperiod}; Interest Rate% (list): {self._n_ir}; Term Period (Years): {self._n_term_end}"
        return f"{self.totalperiod}; {self.loanpackage}"
        
        
## for testing
# print(help(LoanPackage))
# ir_package1=[1.38]
# TestA=LoanPackage(30,ir_package1)
# TestA.n_term_end=[0]
# print(TestA)
# print(TestA.n_ir)
# print("n_term_end",TestA.n_term_end,type(TestA.n_term_end))

# answer=TestA.generate_ix_table(ir_package1)
# print(len(answer),answer)
# print(TestA)

# ir_package1=[1.38]
# TestAA=LoanPackage(30,ir_package1)
# # TestAA.n_term_end=[0]
# print(TestAA)
# print(TestAA.n_ir)
# print("n_term_end",TestAA.n_term_end,type(TestAA.n_term_end))

# answer=TestAA.generate_ix_table(ir_package1)
# print(len(answer),answer)
# print(TestAA)


# ir_package1=[1.39,1.48,2.3]
# TestB=LoanPackage(30,ir_package1)
# TestB.n_term_end=[1,5,6]
# print(TestB)

# answer=TestB.generate_ix_table(ir_package1)
# print(len(answer),answer)


# ir_package1=[1.68,1.8]
# TestC=LoanPackage(30,ir_package1)
# TestC.n_term_end=[5,6,0]
# print(TestC)

# answer=TestC.generate_ix_table(ir_package1)
# print(len(answer),answer)

# ir_package1=[1.38,1.58,1.98,6]
# TestD=LoanPackage(30,ir_package1)
# TestD.n_term_end=[1,2,3,4]
# print(TestD)

# answer=TestD.generate_ix_table(ir_package1)
# print(len(answer),answer)


# # # for testing (further)
# print("====/=====================/============/===========/=============")
# ir_package1="1.38"
# print(type(ir_package1))
# Test_String=LoanPackage(30,ir_package1)
# # Test_String.n_term_end="0"
# print(Test_String)
# print("Test_String.n_ir",Test_String.n_ir, type(Test_String.n_ir))

# print("Test_String.n_term_end",Test_String.n_term_end,type(Test_String.n_term_end))
# answer=Test_String.generate_ix_table(Test_String.n_ir)
# print(len(answer),answer)
# print(Test_String)