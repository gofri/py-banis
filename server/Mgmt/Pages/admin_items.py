#!/usr/bin/python3.6
# encoding: utf-8

from Mgmt.Gui import generator as Generator
from flask import render_template
from DL.admin_items import fetch_items as fetch_items_from_db

class AdminItems(object):
    def __init__(self):
        items = fetch_items_from_db()

    def html(self):
        return render_template('admin_items.html', **self.__content_dict())

    def __item_groups(self):
        pass
    
    def __content_dict(self):
        return {'layout': self.Content().sub_pages(), }
    
    class Content(object):
        SUB_PAGES = [
            {'title':'ניהול לקוחות',  'href':'admin_customers', },
            {'title':'ניהול משתמשים',  'href':'admin_users', },
            {'title':'ניהול מוצרים',  'href':'admin_items', },
        ]

        def sub_pages(self):
            return self.SUB_PAGES