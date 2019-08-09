#!/usr/bin/python3.6
# encoding: utf-8

import copy
from Mgmt.users import Perms
from Mgmt.Gui import generator as Generator
from flask import render_template

class Login(object):
    def __init__(self, perm):
        self.perm = perm

    def html(self):
        return render_template('login.html', **self.content_dict())
    
    class Content(object):
        LAYOUT = {
            Perms.GUEST: { 
                'form_prop': { 'submit_text':'התחבר',  }, 
                'inputs': [
                    {'title':'שם משתמש',  'type':'text', 'name':'username', },
                    {'title':'סיסמה',  'type':'password', 'name':'password', },
                ]
            },
            Perms.USER: {
                'form_prop': { 'submit_text':'התנתק',  }, 
            },
            Perms.ADMIN: {
                'form_prop': { 'submit_text':'התנתק',  }, 
            }, 
        }

        def __init__(self, perm):
            self.perm = perm

        @property
        def form(self):
            return self.LAYOUT[self.perm]

        @property
        def form_prop(self):
            return self.form['form_prop']
        
        @property
        def submit_text(self):
            return self.form_prop['submit_text']

        @property
        def inputs(self):
            return self.form['inputs'] if 'inputs' in self.form.keys() else []

    def __form(self):
        content = self.Content(self.perm)
        html = Generator.generate_inputs(content.inputs)
        
        return Generator.generate_form('login', content=html, submit_text=content.submit_text)
    
    def content_dict(self):
        return {'form': self.__form(), }