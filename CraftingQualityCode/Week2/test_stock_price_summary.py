import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_stock_price_summary1(self):
        """ Test a random list of numbers. """
        self.assertEqual(a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0,
                                                 0, 0.10, -0.01]),
                         (0.14, -0.17))
    def test_stock_price_summary2(self):
        """ Test a list of all zeros. """
        self.assertEqual(a1.stock_price_summary([0.00, 0.00, 0.00, 0.00, 0, 0,
                                                 0.00, 0.00]), (0, 0))

    def test_stock_price_summary3(self):
        """ Test a list of all megative numbers. """
        self.assertEqual(a1.stock_price_summary([-0.01, -0.03, -0.02, -0.14,
                                                 -0.11, -0.01, -0.10, -0.01]),
                         (0, -0.43))

if __name__ == '__main__':
    unittest.main(exit=False)
