#!/usr/bin/python3.6
# encoding: utf-8
from . import common

COLLECTION_KEY = 'ADMIN_ITEMS'

def fetch_items():
    data = common.DB.ins().get_collection(COLLECTION_KEY).find()
    return data

def put_items(items):
    data = common.DB.ins().insert(COLLECTION_KEY, 'he', 'lo')
    return data