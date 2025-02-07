#!/usr/bin/env python3
"""
Class for encoding ?
"""

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
