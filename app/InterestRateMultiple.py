
from app.InterestRateMarket import InterestRateMarket
# from InterestRateMarket import InterestRateMarket

class InterestRateMultiple(InterestRateMarket):
    '''This is InterestRateMultiple Class that take in a list of interest rate (annual) and a list of term period (years)
       to dissect and recompute the monthly payment
    
    '''
    def __init__(self, given_annual_rate_list, given_term_period_list):
        self.given_annual_rate_list = given_annual_rate_list
        self.given_term_period_list = given_term_period_list
        self.given_monthly_rate_list = given_annual_rate_list
        
    # property getter
    @property
    def given_monthly_rate_list(self):
        return self._given_monthly_rate_list
        
    # property setter
    @given_monthly_rate_list.setter
    def given_monthly_rate_list(self, value):
        print("setter monthly rate")
        if isinstance(value, str) and value != "":
            # print("this is string value")
            float_list=self.string_to_float_list(value)
            if isinstance(float_list, list):
                self._given_monthly_rate_list = [InterestRateMarket(x).compute_monthly for x in float_list]
            else:
                self._given_monthly_rate_list =[InterestRateMarket(float_list).compute_monthly]
        elif isinstance(value, float) and value != "":
            self._given_monthly_rate_list = InterestRateMarket(value).compute_monthly
            
        elif isinstance(value, list) and value != "":
            self._given_monthly_rate_list = [InterestRateMarket(x).compute_monthly for x in value]
            
            
            
            
    # property getter
    @property
    def given_annual_rate_list(self):
        print("getter")
        return self._given_annual_rate_list
    
    # property setter
    @given_annual_rate_list.setter
    def given_annual_rate_list(self, value):
        print("setter annual rate")
        if isinstance(value, str):
            float_list=self.string_to_float_list(value)
            if isinstance(float_list, list):
                self._given_annual_rate_list = [float(x)/100 for x in float_list]
            else:
                self._given_annual_rate_list = [float_list]
        elif isinstance(value, float) and value != "":
            self._given_annual_rate_list = value/100
            
        elif isinstance(value, list) and value != "":
            self._given_annual_rate_list = [x/100 for x in value]




    ## this function is used to convert string for interest rate to float list
    def string_to_float_list(self,string_list):
        print(type(string_list))
        if isinstance(string_list, str):
            if "," not in string_list:
                return float(string_list)
            else:
                string_list=string_list.split(",")
                return [float(x) for x in string_list]

    ## this function is used to convert string for term period to int list
    def string_to_int_list(self,string_list):
        print(type(string_list))
        if isinstance(string_list, str):
            if "," not in string_list:
                return int(string_list)
            else:
                string_list=string_list.split(",")
                return [int(x) for x in string_list]


    # property getter
    @property
    def given_term_period_list(self):
        print("getter")
        return self._given_term_period_list
    
    # # property setter
    # @given_term_period_list.setter
    # def given_term_period_list(self, value):
        # print("DEBUG",value,type(value))
        # self._given_term_period_list = value
            



    # property setter
    @given_term_period_list.setter
    def given_term_period_list(self, value):
        print("DEBUG",value,type(value))
        if isinstance(value, str)and value != "":
            print("DEBUG in string term period")
            int_list=self.string_to_int_list(value)
            print("int_list",int_list,type(int_list))
            if isinstance(value, int)and value != "":
                print("---int_list stage1---")
                self._given_term_period_list = int(int_list)
            elif isinstance(int_list, list):
                # self._given_term_period_list = [float(x)/100 for x in float_list]
            # else:
                print("---int_list stage2---")
                self._given_term_period_list = int_list
            else:
                self._given_term_period_list = value
        elif isinstance(value, int) or isinstance(value, list) and value != "":
            self._given_term_period_list = value
            
            
        # # if isinstance(value, list) and len(self._given_term_period_list)>0 and not (len(self._given_term_period_list) <= len(self._given_annual_rate_list)):
            # # print("length NOT EQUAL, please check input")
            # # self._given_term_period_list = self._given_term_period_list[:len(self._given_annual_rate_list)]




    def __str__(self):
        print(f"-"*50)
        return (f"Given Rate (Annual): {self._given_annual_rate_list}; Given Term (Years): {self._given_term_period_list}; Monthly rates {self._given_monthly_rate_list}") 




# # # Testing Case 1
# print("# # Testing Case 1")
# ir_testpackage=[1.39,1.48,2.3]
# ir_testpackage=1.39
# # n_term_end_testpackage=[1,5,6]
# n_term_end_testpackage=3
# print(type(ir_testpackage),type(n_term_end_testpackage))

# testA=InterestRateMultiple(ir_testpackage,n_term_end_testpackage)
# testA.given_annual_rate_list
# testA.given_term_period_list
# # print(testA)
# # print(help(testA))
# print("monthly==============")
# print(testA.given_monthly_rate_list)


# # # Testing with String - TEST 1
# print("# # Testing with String - TEST 1")
# ir_testpackage="1.39,1.48,2.3"
# n_term_end_testpackage="1,5,6"

# testA=InterestRateMultiple(ir_testpackage,n_term_end_testpackage)
# print("testA.given_annual_rate_list",testA.given_annual_rate_list, type(testA.given_annual_rate_list))
# print("testA.given_term_period_list",testA.given_term_period_list,type(testA.given_term_period_list))

# print(testA)

# print("monthly==============")
# print(testA.given_monthly_rate_list)


# # # # Testing with String - TEST 2
# print("=============================# # # Testing with String - TEST 2====================================")
# ir_testpackage="1.39"
# n_term_end_testpackage="3"

# testA=InterestRateMultiple(ir_testpackage,n_term_end_testpackage)
# print("testA.given_annual_rate_list",testA.given_annual_rate_list, type(testA.given_annual_rate_list))
# print("testA.given_term_period_list",testA.given_term_period_list,type(testA.given_term_period_list))
# testA.given_term_period_list
# print(testA)

# print("monthly==============")
# print(testA.given_monthly_rate_list)