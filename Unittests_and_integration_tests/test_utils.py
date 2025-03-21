#!/usr/bin/env python3

import unittest
from parameterized import parameterized

from unittest import TestCase

import utils


class TestAccessNestedMap(TestCase):
    """ Unittest class for utils"""
    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    def test_access_nested_map_exception(self, nested_map, path):
        self.assertRaises(utils.access_nested_map(nested_map, path), KeyError)


if __name__ == '__main__':
    unittest.main()
