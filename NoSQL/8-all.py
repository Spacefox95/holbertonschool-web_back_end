#!/usr/bin/env python3
"""
List all documents in a collection
"""


def list_all(mongo_collection):
    """ List documents """
    return mongo_collection.find()
