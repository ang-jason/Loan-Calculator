import unittest
from unittest.mock import patch
from interest_rate_market import InterestRateMarket


class TestInterestRateMarket(unittest.TestCase):
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
        self.rate1 = InterestRateMarket(1.39)
        self.assertEqual(self.rate1.given_annual_rate, 0.0139)
        self.assertAlmostEqual(self.rate1.compute_monthly, 0.00115833333333333)

    def test_initialisation2(self):
        print('Setting up the class with inputs')
        self.rate2 = InterestRateMarket(1.39,365,30)
        self.assertEqual(self.rate1.given_annual_rate, 0.0139)
        self.assertAlmostEqual(self.rate2.compute_monthly, 0.00114246575342466)

    def test_initialisation2(self):
        print('Setting up the class with inputs')
        self.rate3 = InterestRateMarket(1.39,360,30)
        self.assertEqual(self.rate3.given_annual_rate, 0.0139)
        self.assertAlmostEqual(self.rate3.compute_monthly, 0.00115833333333333)

if __name__ == '__main__':
    unittest.main()
