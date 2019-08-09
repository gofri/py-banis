#!/usr/bin/python3.6
# encoding: utf-8
class Perms(object):
    NAMES = ["guest", "user", "admin"]
    GUEST = 0
    USER = 1
    ADMIN = 2

    @classmethod
    def sanity_check(cls, perm):
        assert 0 <= perm < len(Perms.NAMES) 

# TODO replace with flask-login
class User(object):
    def __init__(self, name='', pwd='', locked_objs=None):
        self.name = name
        self.pwd = pwd
        self.locked_objs = locked_objs or []

    def register_locked_obj(self, lock):
        self.locked_objs.append(lock)

    def unregister_locked_obj(self, lock):
        self.locked_objs.remove(lock)

class Users(object):
    def __init__(self, users=None):
        self.users = users or []
    
    def who_locks(self, obj):
        for u in self.users:
            if obj in [l.pick_obj() for l in self.users.locked_objs]:
                return u.name
        return None

    def get_user(self, name, passwd=None):
        for u in self.users:
            if u.name == name:
                if (not passwd) or u.passwd == passwd:
                    return u
        return None