#!/usr/bin/env python3
""" Test file for client"""

import unittest
from unittest.mock import PropertyMock, patch
from parameterized import parameterized


from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Unit test class for GithubOrgClient """

    @parameterized.expand([
        ("google",),
        ("abc",)
        ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ Test GithubOrg returns correct value"""

        mock_get_json.return_value = {"login": org_name}

        client = GithubOrgClient(org_name)

        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, {"login": org_name})

    def test_public_repos_url(self):
        mocked_payload = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"}

        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = mocked_payload
            client = GithubOrgClient("test_org")
            result = client._public_repos_url

            mock_org.assert_called_once()
            self.assertEqual(result, mocked_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Test public_repos method"""

        mocked_payload = [
            {"name": "choice1"},
            {"name": "choice2"},
            {"name": "choice3"}
        ]
        mock_get_json.return_value = mocked_payload

        mocked_repos_url = "https://api.github.com/orgs/test_org/repos"

        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = mocked_repos_url

            client = GithubOrgClient("test_org")
            result = client.public_repos()

            expected = ["choice1", "choice2", "choice3"]
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(mocked_repos_url)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
