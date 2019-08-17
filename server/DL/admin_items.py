#!/usr/bin/python3.6
# encoding: utf-8
from . import common

COLLECTION_KEY = 'ADMIN_ITEMS'

def fetch_items():
    data = common.DB.ins().get_collection(COLLECTION_KEY)
    print(data.found_one())
    return data

def put_items(items):
    data = common.DB.ins().collections.set(COLLECTION_KEY)
    return data