# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 06:32:24 2013

@author: localadmin
"""

from pymongo import MongoClient


def connect_to_db(db_name="test"):
    """(str) -> object
    This function return MongoDB Database connection.
    Parametr db_name is string, name of databes
    """
    connection = MongoClient(host="mongodb://localhost", port=27017)
    db = connection[db_name]
    
    return db

    
def case_collection(db_name, collection_name):
    """(str, str) -> MongoDb_Collection
    return MongoDB Collection cursor
    """
    return connect_to_db(db_name)[collection_name]


if __name__ == '__main__':
    #print connect_to_db("workshop")
    print case_collection("workshop", "messages")
