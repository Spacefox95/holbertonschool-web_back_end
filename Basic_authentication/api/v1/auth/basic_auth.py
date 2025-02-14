#!/usr/bin/env python3
"""
Class for encoding ?
"""

import base64
import binascii
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


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

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
            ) -> TypeVar('User'):
        """ Extract the user credentials"""
        if user_email is None or user_pwd is None:
            return None
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None
        try:
            user_creds = User.search({"email": user_email})
        except Exception:
            return None
        if not user_creds or len(user_creds) == 0:
            return None
        user = user_creds[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user
