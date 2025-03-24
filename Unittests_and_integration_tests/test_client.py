#!/usr/bin/env python3
""" Test file for client"""

import unittest
from unittest.mock import MagicMock, PropertyMock, patch
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


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
        """ Test public_repos_url method"""

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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test the has_license method"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    ("org_payload", TEST_PAYLOAD.org_payload),
    ("repos_payload", TEST_PAYLOAD.repos_payload),
    ("expected_repos", TEST_PAYLOAD.expected_repos),
    ("apache2_repos", TEST_PAYLOAD.apache2_repos),
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """ Patch requests.et and dynamically extract fixtures"""
        cls.org_payload = TEST_PAYLOAD[0][0]
        cls.repos_payload = TEST_PAYLOAD[0][1]
        cls.expected_repos = [repo["name"] for repo in cls.repos_payload]
        cls.apache2_repos = [
            repo["name"] for repo in cls.repos_payload
            if repo.get("license") and repo["license"]["key"] == "apache-2.0"]

        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            mock_response = MagicMock()
            if url == "https://api.github.com/orgs/google":
                mock_response.json.return_value = cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                mock_response.json.return_value = cls.repos_payload
            return mock_response

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patching"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Test public_repos return correct repo names"""
        client = GithubOrgClient("google")
        result = client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """ Test filtering public repo by Apach license"""
        client = GithubOrgClient("google")
        result = client.public_repos(license="apache-2.0")
        self.assertEqual(result, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
