#!/usr/bin/env python3
""" List of school having a specific topic. """

def schools_by_topic(mongo_collection, topic):
    """ Based on the given topic in the argument list all
        all the document.
    """
    mongo_collection.find({"topics": topics})
