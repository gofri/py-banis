#!/usr/bin/python3.6
# encoding: utf-8

import json

def jsonize(obj):
    return json.dumps(obj, indent=2, default=default_json)

def default_json(obj):
    if not has_something(obj):
        return default_entry(obj)
    else:
        return {'type':type_name(obj), 'data':obj.__dict__}

def default_entry(obj):
    return {'type':'DEFAULT', 'data':type_name(obj)}

def type_name(obj):
    t = type(obj)
    return t.__name__ + '.' + t.__module__

def get_dict_like(obj):
    if is_instance(obj):
        return vars(obj).items()
    elif type(obj) is dict:
        return obj.items()
    else:
        return None

def has_something(obj):
    dict_vals = get_dict_like(obj)
    if dict_vals is not None:
        return any(has_something(v) for _,v in dict_vals)
    elif type(obj) in (tuple, list):
        return bool(obj) and any(has_something(x) for x in obj)
    elif type(obj) is int:
        return True
    else:
        return bool(obj)

def is_instance(obj):
    try:
        obj.__dict__
    except Exception:
        return False
    else:
        return True