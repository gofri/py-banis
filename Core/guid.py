#!/usr/bin/python3.6
# encoding: utf-8

import base64
import uuid

def __get_uuid():
    return uuid.uuid4().bytes

def get_guid(b64=None):
    if b64:
        r_uuid = base64.urlsafe_b64decode(b64)
        return r_uuid.replace('=', '')
    else:
        return __get_uuid()

def get_guid_b64(guid=None):
    r_uuid = base64.urlsafe_b64encode(guid or __get_uuid())
    return r_uuid.replace('=', '')
