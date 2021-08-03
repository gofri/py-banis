#!/usr/bin/python3.6
# encoding: utf-8

from . import utils

def ItemType():
    ''' A unique item type. '''
    def __init__(self, name='', icon=None, desc=''):
        self.name = name
        self.icon = icon
        self.desc = desc

### Grouping

class ItemGroup(object):
    ''' A collection of items. '''
    def __init__(self, name='', entries=None):
        self.name = name
        self.entries = entries or []

    def move_entry(self, *args, **kwargs):
        return utils.list_move_entry(self.entries, *args, **kwargs)

    @classmethod
    def combine(cls, g1, g2, new_name=''):
        return cls(name=new_name, entries=utils.unique_combine(g1.entries, g2.entries))

class ItemMultiGroup(object):
    ''' A collection of groups. '''
    def __init__(self, groups=None):
        self.groups = groups or []

    def append(self):
        self.groups.append(ItemGroup())

    def remove(self, index):
        self.groups.pop(index)

    def combine(self, g1_index, g2_index, *args, **kwargs):
        g1 = self.groups[g1_index]
        g2 = self.groups[g2_index]
        self.add_new(ItemGroup.combine(g1, g2, *args, **kwargs))

    def move_entry(self, *args, **kwargs):
        return utils.list_move_entry(self.groups, *args, **kwargs)

### Counting

class ItemEntryData(object):
    ''' The data of a single item. '''
    def __init__(self, serial='', category_num='', other=''):
        self.serial = serial
        self.category_num = category_num # TODO TBD: does category belong to ItemType?
        self.other = other

class ItemCountingEntry(object):
    ''' A single entry of an item. '''
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
