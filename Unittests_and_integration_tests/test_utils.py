#!/usr/bin/env python3

import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized

from unittest import TestCase

import requests

import utils


class TestAccessNestedMap(TestCase):
    """ Unittest class for utils.access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])

    def test_access_nested_map_exception(self, nested_map, path, expected_key):
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

if __name__ == '__main__':
    unittest.main()
