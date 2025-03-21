#!/usr/bin/env python3

import unittest
from parameterized import parameterized

from unittest import TestCase


class TestAccessNestedMap(TestCase):
    """ Unittest class for utils"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(self.access_nested_map(nested_map, path), expected)


if __name__ == 'main':
    unittest.main()
