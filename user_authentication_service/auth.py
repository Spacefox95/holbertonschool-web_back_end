#!/usr/bin/env python3

""" Password hashing function"""

from typing import Optional
import uuid
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ Transform the password in bytes and hash it"""
    byte_password = str.encode(password)
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(byte_password, salt)

    return hashed


def _generate_uuid() -> str:
    """ Generate a uuid"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register a user"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            new_user_password = _hash_password(password)
            new_user = self._db.add_user(email, new_user_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """ Check the user exist"""
        try:
            valid_user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        hashed_password = valid_user.hashed_password
        if isinstance(hashed_password, str):
            hashed_password = hashed_password.encode("utf-8")

        return bcrypt.checkpw(
            password.encode('utf-8'), hashed_password)

    def create_session(self, email: str) -> str:
        """ Create a user session_id"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user_id=user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Optional[User]:
        """ Get a user from the session_id"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

        return user

    def destroy_session(self, user_id: int) -> None:
        """ Detroy the user session"""
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """
        Generates a reset password token for a user.

        Args:
            email (str): the user's email.

        Returns:
            str: the generated reset password token.
        """

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)

        return

    def update_password(self, reset_token: str, password: str) -> None:
        """ Update the user's password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError

        hd_pwd = self._hash_password(password)
        self._db.update_user(user.id, hashed_password=hd_pwd, reset_token=None)
