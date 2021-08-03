#!/usr/bin/python3.6
# encoding: utf-8

from Core import item
from Core.logicalock import Ownership

class Site(object):
    ''' A single site (e.g. school). '''
    class SiteInfo(object):
        def __init__(self):
            pass
    
    def __init__(self, info=None, zone=None):
        self.info = info or self.SiteInfo()
        self.zone = zone or Zone()

class Zone(object):
    ''' A zone within a site.
        Zones are practically tree nodes (e.g. school->floors->rooms). '''
    class ZoneInfo(object):
        def __init__(self, item_counting=None, desc='', gps_location=None, icon=None):
            self.item_counting = item_counting or item.AtomicItemCounting()
            self.desc = desc
            self.gps_location = None
            self.icon = None

    def __init__(self, name='', info=None, sub_zones=None):
        self.name = name
        self.info = info or self.ZoneInfo()
        self.sub_zones = sub_zones or []

    def add_sub_zone(self, zone=None):
        self.sub_zones.append(zone or Zone())

    def add_sub_zones(self, sub_zones=None):
        for s in sub_zones or ():
            self.add_sub_zone(s)

    @property
    def items_counting(self):
        return self.info.item_counting

    def is_leaf(self):
        return len(self.sub_zones) == 0
    
class ZoneWizard(object):
    ''' Handy helpers for zones creation. probably should be js but could be implemented in backend too. '''
    @classmethod
    def get_floor(cls, first_room=1, count=1, leap=1):
        return [Zone(str(room)) for room in \
                range(first_room, first_room + count, leap)]
    
    @classmethod
    def get_multifloor(cls, first_floor=0, count_floors=1, rooms_per_floor=1, leap=1, width=100):
        return [cls.get_floor(floor * width + 1, rooms_per_floor, leap) for floor in \
                range(first_floor, first_floor + count_floors)]