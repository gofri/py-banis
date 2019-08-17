#!/usr/bin/python3.6
# encoding: utf-8

from Mgmt.auth import Perms
from Mgmt.Gui import generator as Generator
import flask
from flask import render_template
from DL import users as usersDL
from flask_login.utils import current_user, login_user, logout_user
from flask_login.login_manager import LoginManager
from Mgmt import auth
from IPython.nbformat import current

#         # Login and validate the user.
#         # user should be an instance of your `User` class
#         login_user(user)
# 
#         flask.flash('Logged in successfully.')
# 
#         next = flask.request.args.get('next')
#         # is_safe_url should check if the url is safe for redirects.
#         # See http://flask.pocoo.org/snippets/62/ for an example.
#         if not is_safe_url(next):
#             return flask.abort(400)
# 
#         return flask.redirect(next or flask.url_for('index'))
#     return flask.render_template('login.html', form=form)

class LoginPage(object):
    def __init__(self, request):
        self.request = request
        self.next = None
        self.check_form_submittion()

    def check_form_submittion(self):
        form = self.request.form
        submit = form.get('submit', '')
        if submit:
            if submit == 'התחבר':
                try:
                    name = form.get('username')
                    passwd = form.get('password')
                    assert name.strip() and passwd.strip(), "empty name/pass"
                    
                    real_user = usersDL.get_user(name, passwd)
                    assert real_user, 'No such user'
                    real_user = auth.User(**real_user)
                    login_user(real_user)
                    self.next = flask.request.args.get('next')
                except Exception as e:
                    flask.flash('ERROR:' + str(e))

            elif 'התנתק' in submit:
                logout_user()
            else:
                print('wtf?!' + submit)

    def html(self):
        if self.next:
            return flask.redirect(self.next)
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