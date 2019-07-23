#!/usr/bin/python3.6
# encoding: utf-8

from .guid import get_guid
# Unique - item types remain the same throught the program
#          Once updated, all dependent data type should be updated
class ItemType(object):
    class ItemTypeInfo(object):
        def __init__(self, name='', icon=None, desc='', guid=None):
            self.name = name
            self.icon = icon
            self.desc = desc
            self.guid = guid or get_guid()
    
    # TODO remove from here - managing should be done in none-singletone objects
    #      even if I decide to use singletone - the implementation of it should be Singletone.member = Imp()
    @classmethod
    def add_type(cls, info=None):
        try:
            cls.types.add(info or cls.ItemTypeInfo())
        except AttributeError:
            cls.types = []
            cls.add_type(info)
    
    @classmethod
    def remove_type(cls, guid):
        try:
            cls.types = list(filter(lambda t: t.guid != guid, cls.types))
        except Exception:
            pass

class ItemGroup(object):
    def __init__(self, name='', entries=None):
        self.name = name
        self.entries = entries or []

    @classmethod
    def combine(cls, name='', groups=None):
        entries = []
        for g in groups or ():
            entries += g.entries
        return cls(name, entries)

class ItemEntryData(object):
    def __init__(self, serial='', category_num='', other=''):
        self.serial = serial
        self.category_num = category_num
        self.other = other

class AtomicItemCounting(object):
    def __init__(self, type_guid=None, entries=None, note=''):
        self.type = type_guid 
        self.entries = entries or []
        self.note = note
    
    def count(self):
        return len(self.entries)
    
    def add_entry(self, *args, **kwargs):
        self.add_entries(self, 1, *args, **kwargs)
    
    def add_entries(self, count, *args, **kwargs):
        for _ in range(count):
            self.entries.append(ItemEntryData(*args, **kwargs))