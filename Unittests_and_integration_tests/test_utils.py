#!/usr/bin/env python3
""" Test file for utils"""

import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized

from unittest import TestCase

import utils


class TestAccessNestedMap(TestCase):
    """ Unittest class for utils.access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access_nested_map function"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        " OK "
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Unittest class for utils.access_nested_map"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = utils.get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ Unittest class for utils.memoize """
    def test_memoize(self):
        """ Method to test memoization"""
        class TestClass:
            """ Test class """

            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            obj = TestClass()
            res1 = obj.a_property
            res2 = obj.a_property

            self.assertEqual(res1, 42)
            self.assertEqual(res2, 42)

            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
