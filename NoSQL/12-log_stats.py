#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    my_collection = db.nginx
    print("{} logs".format(my_collection.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = my_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    new_method = my_collection.find({"method": "GET", "path": "/status"})
    print("{} status check".format(len(list(new_method))))
