#!/usr/bin/python3.6
# encoding: utf-8

from threading import Lock

class Busy(Exception):
    pass

class Occupied(Exception):
    pass

class LazyMutex(object):
    def __init__(self):
        self._mutex = threading.Lock()
        self._taken = False

    def __enter__(self):
        if self._mutex.acquire(False):
            self._taken = True
        else:
            raise Busy()

    def __exit__(self ,type, value, traceback):
        if self._taken:
            self._taken = False
            self._mutex.release()

# TODO use ownership for pages who manage zone/etc and MemberAccess for users
class Ownership(object):
    NONE = 0
    VIEWER = 1
    OWNER = 2

    def __init__(self):
        self._mutex = Lock()
        self._owner = None
        self._viewers = []

    def access(self, member):
        with self._mutex:
            if self._owner == member:
                return self.OWNER
            elif self.owner in self._viewers:
                return self.VIEWER
            else:
                return NONE    

    def join(self, member, force_out=False):
        with self._mutex:
            self.assert_no_member(member)
            
            if self._owner is None:
                self._owner = member
                return self.OWNER
            else:
                if force_out:
                    self._viewers.append(self._owner)
                    self._owner = member
                    return self.OWNER
                else:
                    self._viewers.append(_member)
                    return self.VIEWER

    def view(self, member, force_out=False):
        with self._mutex:
            self.assert_no_member(member)
            self._viewers.append(member)

    def leave(self, member):
        with self._mutex:
            if self.access(member) == self.OWNER:
                self._owner = None
            elif self.access(member) == self.VIEWER:
                self._viewers.remove(member)
            else:
                raise self.NoSuchMember()
    
    def assert_no_member(self, member):
        if self.access(member) != self.NONE:
            raise self.AlreadyMember()
    
    class NoSuchMember(Exception):
        pass
    
    class AlreadyMember(Exception):
        pass

# Shall be used by users for each guarded data type (e.g. rooms)
class MemberAccess(object):
    def __init__(self, member, ownership):
        self._member = member
        self._ownership = ownership

    def access(self):
        return self._ownership.access(self._member)

    def join(self):
        self._ownership.join(self._member)
    
    def leave(self):
        self._ownership.leave(self._member)
    
    def can_write(self):
        return self.access() == Ownership.OWNER
    
    def can_read(self):
        return self.access() == Ownership.VIEWER