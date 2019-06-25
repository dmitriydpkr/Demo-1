#!/usr/bin/env python3
import unittest
from unittest import TestCase
import fibonacci as fibo


class TestFibForRange(TestCase):

    def test_get_validate_arguments_zero2(self):
        self.assertRaises(ValueError, fibo.get_validate_arguments, 5, 0)

    def test_get_validate_arguments_both(self):
        self.assertRaises(ValueError, fibo.get_validate_arguments, 0, 0)

    def test_get_validate_arguments_equals(self):
        self.assertRaises(ValueError, fibo.get_validate_arguments, 5, 5)

    def test_get_validate_arguments_wrong_order(self):
        self.assertRaises(ValueError, fibo.get_validate_arguments, 40, 39)

    def test_get_validate_arguments_correct(self):
        self.assertTrue(fibo.get_validate_arguments(3, 8))

    def test_create_fibo_range_3_8(self):
        self.assertEqual(fibo.create_fibo_range(3, 8), [2, 3, 5, 8, 13, 21])

    def test_create_fibo_range_1_5(self):
        self.assertEqual(fibo.create_fibo_range(1, 5), [1, 1, 2, 3, 5])


if __name__ == '__main__':
    unittest.main()
