#!/usr/bin/env python3
"""
Insert new documents in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """ Insert kwargs as new doc in a collection """
    post = kwargs
    _id = mongo_collection.insert_one(post)
    return _id.inserted_id
