#!/usr/bin/python3.6
# encoding: utf-8

from Mgmt.Gui import generator as Generator
from flask import render_template

class AdminPanel(object):
    def html(self):
        return render_template('admin_panel.html', **self.__content_dict())

    def __buttons(self):
        return Generator.generate_buttons(self.Content().sub_pages())
    
    def __content_dict(self):
        return {'layout': self.__buttons(), }
    
    class Content(object):
        SUB_PAGES = [
            {'title':'ניהול לקוחות',  'href':'admin_customers', },
            {'title':'ניהול משתמשים',  'href':'admin_users', },
            {'title':'ניהול מוצרים',  'href':'admin_items', },
        ]

        def sub_pages(self):
            return self.SUB_PAGES