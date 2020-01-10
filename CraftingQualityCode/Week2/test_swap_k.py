import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_swap_k1(self):
        """ Initial test using an index of 2 to swap. """
        self.nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(self.nums, 2)
        self.assertEqual(self.nums, [5, 6, 3, 4, 1, 2])

    def test_swap_k_max(self):
        """ Test a case with k at the max allowed value. """
        self.num2 = [1, 2, 3, 4, 5, 6]
        a1.swap_k(self.num2, len(self.num2)//2)
        self.assertEqual(self.num2, [4, 5, 6, 1, 2, 3])

    def test_swap_k_min(self):
        """ Test a case with k at the max allowed value. """
        self.num3 = [1, 2, 3, 4, 5, 6]
        a1.swap_k(self.num3, 0)
        self.assertEqual(self.num3, [1, 2, 3, 4, 5, 6])

    def test_swap_k_empty(self):
        """ Test an empty list. """
        self.num4 = []
        a1.swap_k(self.num4, 2)
        self.assertEqual(self.num4, [])

if __name__ == '__main__':
    unittest.main(exit=False)
