#!/usr/bin/env python3
"""API authentification"""

import os
from typing import List, TypeVar


class Auth:
    """Authentification class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """path for authorization"""
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        slash_path = path if path.endswith("/") else path + "/"
        if slash_path in excluded_paths:
            return False
        print(f"Checking authentication for path: {path}")
        return True

    def authorization_header(self, request=None) -> str:
        """flask request object"""
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar("User"):
        """flask request object"""
        return None

    def session_cookie(self, request=None):
        """session cookie"""
        if not request:
            return None
        session_name = os.getenv("SESSION_NAME", "_my_session_id")

        return request.cookies.get(session_name)
