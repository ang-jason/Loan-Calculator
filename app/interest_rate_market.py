class InterestRateMarket:
    '''
    This is InterestRateMarket Class that take in interest rate (annual),
    year_length (optional) and month_length(optional)
    which convert the interest rate to monthly interest rate
    market convention year_length (12 months)
    or custom conventions which you can specify
    year_length (365,360) and month_length (30)
    This is a very refine class configuration which caters
    to different market conventions if there is any.
    However of what I known have been written to default mode of (12 months)
    '''
    def __init__(self, given_annual_rate, year_length=12, month_length=0):
        self.given_annual_rate = given_annual_rate/100.0
        self.year_length = year_length
        self.month_length = month_length

    # property getter
    @property
    def given_annual_rate(self):
        return self._given_annual_rate

    # property setter
    @given_annual_rate.setter
    def given_annual_rate(self, value):
        if isinstance(value, float) and value != "":
            self._given_annual_rate = value

    # property getter
    @property
    def year_length(self):
        return self._year_length

    # property setter
    @given_annual_rate.setter
    def year_length(self, value):
        if isinstance(value, int) and value != "":
            self._year_length = value

    # property getter
    @property
    def month_length(self):
        return self._month_length

    # property setter
    @month_length.setter
    def month_length(self, value):
        if isinstance(value, int) and value != "":
            self._month_length = value

    @property
    def compute_monthly(self):
        if self._year_length > 0 and self._month_length > 0:
            return float(self._given_annual_rate/self._year_length*self._month_length)
        else:
            # print(given_annual_rate)
            return float(self._given_annual_rate/self._year_length)

    # def __div__(self, other):
    #     return self/other

    def __str__(self):
        print(f"-"*50)
        return (f"Given Rate (Annual): {self._given_annual_rate}; Year Length: {self._year_length}; Month Length: {self._month_length} Monthly Rate: {self.compute_monthly:.5f}")

# TESTING

# testA=InterestRateMarket(1.39)
# print(testA)
# print(testA.given_annual_rate,type(testA.given_annual_rate))
# print(testA.compute_monthly,type(testA.compute_monthly)) ### 0.00115833333333333
# assert round(testA.compute_monthly,10) == round(0.00115833333333333,10)

# testB=InterestRateMarket(1.39,365,30)
# print(testB)
# print(testB.given_annual_rate,type(testB.given_annual_rate))
# print(testB.compute_monthly,type(testB.compute_monthly)) ### 0.00114246575342466
# assert round(testB.compute_monthly,10) == round(0.00114246575342466,10)

# # 0.00115833333333333
# testC=InterestRateMarket(1.39,360,30)
# print(testC)
# print(testC.given_annual_rate,type(testC.given_annual_rate))
# print(testC.compute_monthly,type(testC.compute_monthly)) ## 0.00115833333333333
# assert round(testC.compute_monthly,10) == round(0.00115833333333333,10)
