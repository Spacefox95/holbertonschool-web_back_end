#!/usr/bin/env python3

""" Password hashing function"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """ Transform the password in bytes and hash it"""
    byte_password = str.encode(password)
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(byte_password, salt)

    return hashed
