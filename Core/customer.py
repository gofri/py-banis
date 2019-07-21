#!/usr/bin/python3.6
# encoding: utf-8

class Customer(object):
    class CustomerInfo(object):
        def __init__(self, name='', phone='', pic=None, mail='', notes=''):
            self.name = name
            self.phone = phone
            self.pic = pic
            self.mail = mail
            self.notes = ''

    def __init__(self, info=None, zones=None, counts=None):
        self.info = info or self.CustomerInfo()
        self.zones = zones or []
        self.counts = counts or []