#!/usr/bin/python3.6
# encoding: utf-8
from . import database

COLLECTION_KEY = 'ADMIN_ITEMS'

def fetch_items():
    data = database.DB.ins().get_collection(COLLECTION_KEY).find()
    return data

def put_items(items):
    data = database.DB.ins().insert(COLLECTION_KEY, 'he', 'lo')
    return data