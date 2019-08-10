#!/usr/bin/python3.6
# encoding: utf-8

import copy
from Mgmt.users import Perms
from Mgmt.Gui import generator as Generator
from flask import render_template

class Home(object):
    def __init__(self, perm):
        self.perm = perm

    def html(self):
        return render_template('home.html', **self.content_dict())
    
    class Content(object):
        SUB_PAGES = {
            Perms.GUEST: [ 
                {'title':'התחבר',  'href':'login', },
            ],
            Perms.USER: [
                {'title':'ספירות פעילות',  'href':'active_counts', },
            ],
            Perms.ADMIN: [
                {'title':'ספירות פעילות',  'href':'active_counts', },
                {'title':'פאנל ניהול',  'href':'admin_panel', }
            ],
        }
        
        def get_sub_pages(self, perm):
            Perms.sanity_check(perm)
            return copy.deepcopy(self.SUB_PAGES[perm])

    def __buttons(self):
        return Generator.generate_buttons(self.Content().get_sub_pages(self.perm))
    
    def content_dict(self):
        return {'layout': self.__buttons(), }