"""Tests for stats.py"""
import unittest
from stats import median, mean

class TestStats(unittest.TestCase):
    def test_median_odd_length(self):
        # 奇数长度，标准中位数
        self.assertEqual(median([1, 3, 2]), 2)
        self.assertEqual(median([5, 1, 9, 3, 7]), 5)
        self.assertEqual(median([10, 20, 30, 40, 50]), 30)

    def test_median_even_length(self):
        # 偶数长度，平均中两个中间值
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        self.assertEqual(median([10, 20, 30, 40]), 25.0)

    def test_median_two_elements(self):
        # 两个元素
        self.assertEqual(median([5, 1]), 3.0)
        self.assertEqual(median([100, 200]), 150.0)

    def test_median_unsorted_input(self):
        # 乱序输入
        self.assertEqual(median([3, 1, 4, 2]), 2.5)
        self.assertEqual(median([9, 2, 7, 5, 1]), 5)

    def test_mean_unchanged(self):
        # 确保 mean 行为未被修改
        self.assertEqual(mean([1, 2, 3]), 2.0)
        self.assertEqual(mean([2, 4, 6, 8]), 5.0)

if __name__ == '__main__':
    unittest.main()
