#!/usr/bin/env python3
""" Hash password for security"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ Hashing function """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Check is the given password matches the hashed password"""
    return bcrypt.checkpw(password.encode(), hashed_password)
