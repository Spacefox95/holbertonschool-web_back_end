#!/usr/bin/env python3
""" Hash password for security"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ Hashing function """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)
