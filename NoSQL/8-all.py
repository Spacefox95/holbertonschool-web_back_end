#!/usr/bin/env python3
"""
List all documents in a collection
"""
import pprint


def list_all(mongo_collection):
    """ List documents """
    for doc in mongo_collection.find():
        pprint.pprint(doc)
