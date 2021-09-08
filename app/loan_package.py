# from total_period import TotalPeriod
# from tnterest_rate_multiple import InterestRateMultiple

from app.total_period import TotalPeriod
from app.interest_rate_multiple import InterestRateMultiple


class LoanPackage():
    '''
    Expanding for the default Loan Class which allows only single interest rate
    This class allow list of interest rates and term period
    as described detailedly in InterestRateMultiple class
    Key element is the generate_ix_table which allow usage
    of setting up arrays of respective interest rates and associated periods.
    e.g. IR=1.35,1.5,1.8
        Term=2,3,4
    [1.35 --- x12 (for year1), 1.35 x12 (for year 2),
    1.5,1.5.. x12 (for year 3), 1.8 ... x12 for (year4),
    1.8... end of the total period]
    Tenor input is to govern the total length ie 30 years
    will have 30*12=360 associated interest rates which
    first 12 will be 1.35, next 12 will be 1.35 and 1.5 following 12
    and 1.8 for year4's 12 and until the end of loan length
    A Basic getter functions to get inputted parameters.
    Input values were governed by InterestRateMultiple
    and TotalPeriod as there were class instances in them.
    '''
    def __init__(self, tenor, n_ir, n_term_end=[0]):
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

    # property setter
    @n_term_end.setter
    def n_term_end(self, value):
        # if (isinstance(value, int) or isinstance(value, list))  and value != "":
        if value != "":
            self.loanpackage.given_term_period_list = value

    def generate_ix_table(self, n_table):
        # print("n_table",n_table,type(n_table))
        # print("self.n_term_end",self.n_term_end,type(self.n_term_end))
        if isinstance(self.n_term_end, float):
            self.n_term_end = [0]
            # self.n_term_end.append(int(0))
            # print("self.n_term_end",self.n_term_end,type(self.n_term_end))

        ir_table = []
        for each in range(0, len(n_table)):
            # print(each)
            # print(n_table[each],self._n_term_end[each])
            if each == 0:
                ir_table.append([n_table[each]]*(self.n_term_end[each])*12)
            else:
                ir_table.append([n_table[each]]*((self.n_term_end[each]-each)*12))

        # print(ir_table)

        # for debug
        # for each_row in ir_table:
        #     print("row",len(each_row))

        flat_list = [item for sublist in ir_table for item in sublist]

        # print(len(flat_list),self.totalperiod.total_period-len(flat_list))

        for each_again in range(len(flat_list), self.totalperiod.total_period):
            flat_list.append(n_table[each])
        # print(flat_list)
        return flat_list

    def __str__(self):
        return f"{self.totalperiod}; {self.loanpackage}"

