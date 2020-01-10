import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_num_buses1(self):
        """ Test value for multiple busses that includes a remainder. """
        self.assertEqual(a1.num_buses(75), 2)

    def test_num_buses2(self):
        """ Test case with no remainder. """
        self.assertEqual(a1.num_buses(100), 2)

    def test_num_buses3(self):
        """ Test a small number. """
        self.assertEqual(a1.num_buses(1), 1)

    def test_num_buses4(self):
        """ Test a larger number. """
        self.assertEqual(a1.num_buses(201), 5)


if __name__ == '__main__':
    unittest.main(exit=False)
