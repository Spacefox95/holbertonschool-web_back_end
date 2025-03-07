#!/usr/bin/env python3

""" Password hashing function"""

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
