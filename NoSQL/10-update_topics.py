#!/usr/bin/env python3
"""
Changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """ Changes topics of a document based on the name """
    # Filter
    filter = {"name": name}
    # Update
    set_topic = {"$set": {"topics": topics}}
    # Add
    result = mongo_collection.update_many(filter, set_topic)
    return result
