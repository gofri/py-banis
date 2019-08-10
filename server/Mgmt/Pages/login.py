#!/usr/bin/python3.6
# encoding: utf-8

import copy
from Mgmt.users import Perms
from Mgmt.Gui import generator as Generator
from flask import render_template, request

class Login(object):
    def __init__(self, perm):
        self.perm = perm
        self.url_args = request.args
        self.content = self.Content(self.perm)
        
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
                'form_prop': { 'submit_text': 'התנתק',  }, 
            },
            Perms.ADMIN: {
                'form_prop': { 'submit_text':'התנתק',  }, 
            }, 
        }

        def __init__(self, perm):
            self.perm = perm

        def layout(self, perm=None):
            return self.LAYOUT[perm or self.perm]

        def form_prop(self, perm=None):
            return self.layout(perm)['form_prop']
        
        def submit_text(self, perm=None):
            return self.form_prop(perm)['submit_text']

        def inputs(self, perm=None):
            return self.layout(perm).get('inputs', [])

    def __layout(self):
        html = Generator.generate_inputs(self.content.inputs())
        
        return Generator.generate_form('login', content=html, submit_text=self.content.submit_text(), method='post')
    
    def content_dict(self):
        return {'layout': self.__layout(), }