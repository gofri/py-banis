from Core import customer

class Customers(object):
    def list_customers(self):
        return {'customers': [
                customer.Customer("a","b").__dict__,
                customer.Customer("c","d").__dict__]
                }