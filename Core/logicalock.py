#!/usr/bin/python3.6
# encoding: utf-8

class LockException(Exception):
    pass

class Logicalock(object):
    def __init__(self, user=None):
        self.user = user

    def lock(self, user):
        if self.is_locked():
            LockException( f'{user} cannot take lock - already used by {self.user}')

        self.user = user
    
    def unlock(self):
        if not self.is_locked():
            LockException(f'Cannot unlock - already unlocked')

        self.user = None
    
    def is_locked(self):
        return self.user is not None

class Lockable(object):
    def __init__(self, obj):
        self.lock = Logicalock()
        self.obj = obj
    
    def get_obj(self, user):
        self.lock.lock(user)
        self.lock.user.register_locked_obj(self)
        return self.obj
    
    def put_obj(self):
        self.lock.user.unregister_locked_obj(self)
        self.lock.unlock()
        
    def pick_obj(self):
        return self.obj