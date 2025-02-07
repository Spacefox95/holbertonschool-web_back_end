#!/usr/bin/env python3
"""
Class for encoding ?
"""

import base64
import binascii
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Class for authentification with basic encoding"""

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """Get the basic authorization"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        extracted = authorization_header.split(" ", 1)
        return extracted[1]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """ Decode the basic authorization"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            b = base64.b64decode(base64_authorization_header)
            return b.decode("utf-8")
        except binascii.Error:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """ Extract the user credentials"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        extracted = decoded_base64_authorization_header.split(":", 1)
        return extracted[0], extracted[1]
