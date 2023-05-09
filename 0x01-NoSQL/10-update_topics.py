#!/usr/bin/env python3
""" Changes all topics of a school document based on the name. """

def update_topics(mongo_collection, name, topics):
    """ Based on the given name as anargument, change the topics
        of the document in a collection.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
