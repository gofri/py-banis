import csv

class CSV(object):
    @classmethod
    def from_dicts(cls, path, headers, data):
        with open(path, 'w') as outf:
            w = csv.DictWriter(outf, headers)
            w.writeheader()
            w.writerows(data)

    @classmethod
    def to_dicts(cls, path):
        with open(path, mode='r') as inf:
            return list(csv.DictReader(inf))
