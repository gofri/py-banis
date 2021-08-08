#!/usr/bin/python3.6
# encoding: utf-8

from Mgmt.Gui import generator as Generator
from flask import render_template
from DL.admin_items import fetch_items, put_items

class Customers(object):
    NEW_CUSTOMER_BUTTON_ID="new_customer_button"
    
    def __init__(self):
        pass

    def html(self):
        return render_template('admin_customers.html', **self.__content_dict())

    def __content_dict(self):
        return {'new_customer_button': self.Content().new_customer_button(), }
    
    class Content(object):
        def new_customer_button(self):
            button = {'title':'לקוח חדש', 'id':'NEW_CUSTOMER_BUTTON_ID', }
            return Generator.generate_buttons([button])