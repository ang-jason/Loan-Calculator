import unittest
from unittest.mock import patch
from loan import Loan



class TestLoan(unittest.TestCase):

    # camelCase due to carry over from legency code
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        # print('setUp')
        # self.emp_1 = Employee('Corey', 'Schafer', 50000)
        # self.emp_2 = Employee('Sue', 'Smith', 60000)
        pass

    def tearDown(self):
        print('tearDown\n')



    def test_initialisation(self):
        print('Setting up the class with inputs')
        
        self.loan1 = Loan(440248, 1.39, 30)
        
        
        self.assertEqual(self.loan1.interest_rate, 1.39)
        self.assertEqual(self.loan1.tenor, 30)
        self.assertEqual(self.loan1.tell_details(),'Loan Amount: $ 440248; Interest Rate (Annual): 1.39 %; Tenor (Years) : 30')
        
    def test_initialisation2(self):
        print('Setting up the class with inputs')
        
        self.loan1 = Loan(440248.0, 1.48, 35)
        
        
        self.assertEqual(self.loan1.interest_rate, 1.48)
        self.assertEqual(self.loan1.tenor, 35)
        self.assertEqual(self.loan1.tell_details(),'Loan Amount: $ 440248.0; Interest Rate (Annual): 1.48 %; Tenor (Years) : 35')
        
        
        
if __name__ == '__main__':
    unittest.main()