import json
from api.customers import Customers

class APILoader(object):
    PREFIX = 'api'
    
    def __init__(self, app):
        self.app = app
        self.customers = Customers()
        self.scheme = [
        {'url':'customers', 'callback':self.customers.list_customers},
    ]

    def add_api_endpoints(self):
        for ep in self.scheme:
            url = '/' + '/'.join([self.PREFIX, ep['url']])
            self.app.route(url)(ep['callback'])