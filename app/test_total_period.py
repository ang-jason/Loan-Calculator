import unittest
from unittest.mock import patch
from total_period import TotalPeriod


class TestTotalPeriod(unittest.TestCase):
    # camelCase due to carry over from legency code
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        pass

    def tearDown(self):
        print('tearDown\n')

    def test_initialisation(self):
        print('Setting up the class with inputs')
        self.duration = TotalPeriod(30)
        self.assertEqual(self.duration.given_tenor, 30)
        self.assertEqual(self.duration.total_period, 360)

    def test_initialisation2(self):
        print('Setting up the class with inputs2')
        self.duration = TotalPeriod(35)
        self.assertEqual(self.duration.given_tenor, 35)
        self.assertEqual(self.duration.total_period, 420)

    def test_initialisation3(self):
        print('Setting up the class with inputs3')
        self.duration = TotalPeriod(35)
        self.assertIsInstance(self.duration.given_tenor, int)
        self.assertIsInstance(self.duration.total_period, int)

if __name__ == '__main__':
    unittest.main()
	
	