#!/usr/bin/python3.6
# encoding: utf-8
import pymongo
from Common import config

class DB(object):
    PROTOCOL = 'mongodb://'
    NAME = 'BanisDB'
    PORT = '27017'
    URL = PROTOCOL + config.site_base_url() + ':' + PORT

    def __init__(self):
        print(self.URL )
        self.client = pymongo.MongoClient(self.URL)
        self.db = self.client[self.NAME]

    def get_collection(self, name, create_if_new=True):
        assert create_if_new or name in self.db.list_collection_names()
        return self.db[name]

    def insert(self, collection, key, value, create_if_new=True):
        assert create_if_new or key in self.db.list_collection_names()
        self.db.get_collection(collection).insert({key:value})

    @classmethod
    def ins(cls):
        try:
            return cls._DB
        except Exception:
            cls._DB = cls()
            return cls._DB