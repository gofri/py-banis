#!/usr/bin/python3.6
# encoding: utf-8

from . import zone

class Count(object):
    class CountInfo(object):
        def __init__(self, name='', start_date=None, end_date=None, notes=''):
            self.name = name
            self.start_date = start_date
            self.end_date = end_date
            self.notes = notes
    
    def __init__(self, info=None, root_zone=None):
        self.info = info or self.CountInfo()
        self.root_zone = root_zone or zone.Zone()