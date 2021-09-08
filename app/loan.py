# Class definition
class Loan:
    '''This is beginner Loan Class that take in loan amount (principal),
    single interest rate (annual), tenor (years) which
    is the duration of whole loan
    Description of the components in a Loan
    A Basic getter and setter functions to
    parameters and the expected data types
    '''
    # Attributes:
    def __init__(self, loan_amount, interest_rate_annual, tenor):
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate_annual
        self.tenor = tenor

    # property getter
    @property
    def loan_amount(self):
        return self._loan_amount

    # property setter
    @loan_amount.setter
    def loan_amount(self, value):
        if isinstance(value, float) or isinstance(value, int) and value != "":
            self._loan_amount = value

    # property getter
    @property
    def interest_rate(self):
        return self._interest_rate

    # property setter
    @interest_rate.setter
    def interest_rate(self, value):
        if value > 0:
            self._interest_rate = value

    # property getter
    @property
    def tenor(self):
        return self._tenor

    # property setter
    @tenor.setter
    def tenor(self, value):
        if isinstance(value, int) and value > 0:
            self._tenor = value

    def tell_details(self):
        display_txt = f"Loan Amount: $ {self._loan_amount}; Interest Rate (Annual): {self._interest_rate} %; Tenor (Years) : {self._tenor}"
        # print(f"Loan Amount: $ {self._loan_amount}")
        # print(f"Interest Rate (Annual): {self._interest_rate} %")
        # print(f"Tenor (Years) : {self._tenor}")
        return display_txt

