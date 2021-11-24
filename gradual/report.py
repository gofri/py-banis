# -*- coding: utf-8 -*-
from csv_converter import CSV
from enum import Enum


class ColHeb(Enum):
    site = 'שם מחסן'
    product = 'שם פריט'
    barcode = 'מספר טבוע'
    count = 'כמות מחשב'

class ReportEntry(object):
    def __init__(self, site, product, barcode, count):
        self.site = site
        self.product = prdouct
        self.barcode = barcode
        self.count = count

    def report_dict(self):
        return {ColHeb[k]:v for k,v in self.__dict__.items()}

class Report(object):
    def __init__(self, path, entries_list):
        self.path = path
        self.reports = [ReportEntry(**kw) for kw in self.entries_list]

    @property
    def headers(self):
        return (col.value for col in ColHeb)

    @property
    def data(self):
        return [r.report_dict() for r in self.reports]

    def to_csv(self):
        CSV.from_dicts(self.path, self.headers, self.data)

    @classmethod
    def from_csv(cls, path):
        data = CSV.to_dicts(path)
        report = cls(path, data)
        return report
