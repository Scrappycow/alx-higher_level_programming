#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_module_dstring(self):
        m= __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)



