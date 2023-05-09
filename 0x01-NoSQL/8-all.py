#!/usr/bin/env python3
""" Lists all documents in a collection """

from pymongo import MongoClinet


def list_all(mongo_collection):
    """ Takes pymongo object as an argument and list all ducoment
        in a collection as list object.
        if the pymongo object is empty it should return empty list
    """
    result = []
    with MongoClient as clinet:
        db = client.my_db
        for doc in db.school.find():
            result.append[doc]
    return result
