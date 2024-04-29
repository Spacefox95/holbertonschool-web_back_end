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
    get = my_collection.find({"method": "GET"})
    post = my_collection.find({"method": "POST"})
    put = my_collection.find({"method": "PUT"})
    patch = my_collection.find({"method": "PATCH"})
    delete = my_collection.find({"method": "DELETE"})
    print(" method GET: {}".format(len(list(get))))
    print(" method POST: {}".format(len(list(post))))
    print(" method PUT: {}".format(len(list(put))))
    print(" method PATCH: {}".format(len(list(patch))))
    print(" method DELETE: {}".format(len(list(delete))))
    method = my_collection.find({"method": "GET", "path": "/status"})
    print("{} status check".format(len(list(method))))
