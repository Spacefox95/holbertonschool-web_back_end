#!/usr/bin/env python3
"""
Class for encoding ?
"""

import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Class for session authentification"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session ID for a given user ID"""
        if not user_id or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
