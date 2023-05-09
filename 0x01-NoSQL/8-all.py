#!/usr/bin/env python3
""" Lists all documents in a collection """

def list_all(mongo_collection):
    """ Takes pymongo object as an argument and list all ducoment
        in a collection.
        if the pymongo object is empty it should return empty list
    """
    documents = mongo_collection.find()
    if documents.count() == 0:
        return []
    return documents
