#!/usr/bin/python3.6
# encoding: utf-8

from Mgmt.auth import Perms
from Mgmt.Gui import generator as Generator
import flask
from flask import render_template
from flask_login.utils import current_user, login_user, logout_user
from flask_login.login_manager import LoginManager
from Mgmt import auth

class LoginPage(object):
    def __init__(self, request, app):
        self.request = request
        self.next = None
        self.app = app
        self.usersDL = self.app.config['DL']['USERS']
        
        self.check_form_submittion()

    def check_form_submittion(self):
        form = self.request.form
        submit = form.get('submit', '')
        if submit:
            if submit == 'התחבר':
                try:
                    name = form.get('username')
                    passwd = form.get('password')
                    assert name.strip() and passwd.strip(), "Empty name or password"
                    
                    user = self.usersDL.get_user(name, passwd)
                    assert user, 'Invalid user or password'
                    
                    user = auth.User(**user)
                    assert login_user(user), "Unexpectedly failed to login"

                    if user not in self.app.config['USERS']: 
                        self.app.config['USERS'].append(user)
                    
                    self.next = 'index'
                except Exception as e:
                    flask.flash('ERROR:' + str(e))
            elif 'התנתק' in submit:
                self.app.config['USERS'].remove(current_user)
                logout_user()
            else:
                print('wtf?!-' + submit + '-')

    def html(self):
        if self.next:
            return flask.redirect(flask.url_for(self.next))
        else:
            return Login(current_user.perm).html()

class Login(object):
    def __init__(self, perm):
        self.perm = perm
        self.content = self.Content(self.perm)
        
    def html(self):
        return render_template('login.html', **self.__content_dict())

    def __layout(self):
        html = Generator.generate_inputs(self.content.inputs())
        return Generator.generate_form('login', content=html, submit_text=self.content.submit_text(), method='post')
    
    def __content_dict(self):
        return {'layout': self.__layout(), }
    
    class Content(object):
        LAYOUT = [
            { 
                'form_prop': { 'submit_text':'התחבר',  }, 
                'inputs': [
                    {'title':'שם משתמש',  'type':'text', 'name':'username', },
                    {'title':'סיסמה',  'type':'password', 'name':'password', },
                    {'title':'נתק משתמש זה ממכשירים אחרים (ניתן להתחבר ממכשיר אחד במקביל)',  'type':'checkbox', 'name':'kickout', 'default':'kickout'},
                ]
            },
            {
                'form_prop': { 'submit_text': 'התנתק',  }, 
            },
            {
                'form_prop': { 'submit_text':'(אדמין) התנתק',  }, 
            }, 
        ]

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
