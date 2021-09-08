class TotalPeriod:
    '''
    This is TotalPeriod Class that take in tenor
    and convert to the total number of payments
    Loan mortgage market convention will be monthly payments.
    Typical tenor will be 30 * (12 month) = 360 number of payments
    This is a foundation class to compute the total length of loan.
    '''
    def __init__(self, given_tenor):
        self.given_tenor = given_tenor

    # property getter
    @property
    def given_tenor(self):
        return self._given_tenor

    # property setter
    @given_tenor.setter
    def given_tenor(self, value):
        if isinstance(value, int) and value != "":
            self._given_tenor = value

    @property
    def total_period(self):
        return self._given_tenor*12

    def __str__(self):
        print(f"-"*50)
        return (f"Years : {self._given_tenor}; Total Period : {self._given_tenor*12}")
