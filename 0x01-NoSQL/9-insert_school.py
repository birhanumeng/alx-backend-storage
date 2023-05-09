#!/usr/bin/env python3
""" Inserts a new document in a collection based on kwargs. """

def insert_school(mongo_collection, **kwargs):
    """ It takes document (python dictionary) object as an argument
        and insert into mongo collection argument, mongo_collection.
    """
    new = mongo_collection.insert(kwargs)
    return new_id
