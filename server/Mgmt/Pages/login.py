#!/usr/bin/python3.6
# encoding: utf-8

import copy
from Mgmt.users import Perms
from Mgmt.Gui import generator as Generator

class Login(object):
    def __init__(self, perm):
        self.perm = perm
    
    class Content(object):
        LAYOUT = {
            Perms.GUEST: { 
                'form': { 'submit_text':'התחבר',  }, 
                'input': [
                    {'title':'שם משתמש',  'type':'text', 'name':'username', },
                    {'title':'סיסמה',  'type':'password', 'name':'password', },
                ]
            },
            Perms.USER: {
                'form': { 'submit_text':'התנתק',  }, 
            },
            Perms.ADMIN: {
                'form': { 'submit_text':'התנתק',  }, 
            }, 
        }

        def get_form(self, perm):
            return copy.deepcopy(self.LAYOUT[perm])

    def __form(self):
        form = self.Content().get_form(self.perm)
        submit_text = form['form']['submit_text']
        
        inputs = form.get('input', [])
        content = Generator.generate_inputs(inputs)
        
        return Generator.generate_form('login', content=content, submit_text=submit_text)
    
    def content_dict(self):
        return {'form': self.__form(), }