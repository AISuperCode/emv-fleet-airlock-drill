import unittest

from stats import median


class TestMedian(unittest.TestCase):
    def test_odd_length(self):
        self.assertEqual(median([5, 9, 1]), 5)

    def test_even_length(self):
        self.assertEqual(median([4, 1, 3, 2]), 2.5)

    def test_two_elements(self):
        self.assertEqual(median([10, 20]), 15.0)

    def test_unsorted_input_is_not_mutated_assumption(self):
        self.assertEqual(median([3, 1, 2]), 2)


if __name__ == "__main__":
    unittest.main()
