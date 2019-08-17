#!/usr/bin/python3.6
# encoding: utf-8

from Mgmt.Gui import generator as Generator
from flask import render_template
from flask_login.utils import current_user

class HomePage(object):
    def __init__(self, request):
        self.request = request
    
    def html(self):
        print(current_user.name, current_user.perm)
        return Home(current_user.perm).html()

class Home(object):
    def __init__(self, perm):
        self.perm = perm

    def html(self):
        return render_template('home.html', **self.__content_dict())

    def __buttons(self):
        return Generator.generate_buttons(self.Content().sub_pages(self.perm))
    
    def __content_dict(self):
        return {'layout': self.__buttons(), }
    
    class Content(object):
        SUB_PAGES = [
            [ {'title':'התחבר',  'href':'login', }, ], # GUEST
            [ {'title':'ספירות פעילות',  'href':'active_counts', }, ], # USER
            [ {'title':'ספירות פעילות',  'href':'active_counts', }, # ADMIN
              {'title':'פאנל ניהול',  'href':'admin_panel', } ],
        ]

        def sub_pages(self, perm):
            return self.SUB_PAGES[perm]
