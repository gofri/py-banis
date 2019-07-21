#!/usr/bin/python3.6
# encoding: utf-8

from Core import item

class Zone(object):
    def __init__(self, name='', sub_zones=None, item_list=None, desc='', gps_location=None, icon=None):
        self.name = name
        self.sub_zones = sub_zones or []
        self.item_counting = item_list or item.ItemCounting()
        self.desc = desc
        self.gps_location = None
        self.icon = None

    def add_sub_zone(self, zone=None):
        assert self.allowed_sub_zones(), 'Cannot add sub zones because there are assigned items'
        self.sub_zones.append(zone or Zone())

    def add_sub_zones(self, sub_zones=None):
        for s in sub_zones or ():
            self.add_sub_zone(s)

    @property
    def items_counting(self):
        assert self.allowed_items(), 'Cannot handle items because there are assigned sub zones'
        return self.item_counting

    def is_leaf(self):
        return len(self.sub_zones) == 0

    def allowed_items(self):
        return self.is_leaf()

    def allowed_sub_zones(self):
        return self.item_counting.count() == 0
    
class ZoneWizard(object):
    @classmethod
    def get_floor(cls, first_room=1, count=1, leap=1):
        return [Zone(str(room)) for room in \
                range(first_room, first_room + count, leap)]
    
    @classmethod
    def get_multifloor(cls, first_floor=0, count_floors=1, rooms_per_floor=1, leap=1, width=100):
        return [cls.get_floor(floor * width + 1, rooms_per_floor, leap) for floor in \
                range(first_floor, first_floor + count_floors)]