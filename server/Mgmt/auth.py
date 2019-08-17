#!/usr/bin/python3.6
# encoding: utf-8
from flask_login import LoginManager, current_user
from flask_login.mixins import UserMixin, AnonymousUserMixin
from DL import users as usersDL
import flask_login

login_manager = LoginManager()

class Perms(object):
    NAMES = ["guest", "user", "admin"]
    GUEST = 0
    USER = 1
    ADMIN = 2

    @classmethod
    def sanity_check(cls, perm):
        assert 0 <= perm < len(Perms.NAMES) 

class AnonUser(AnonymousUserMixin):
    @property
    def perm(self):
        return Perms.GUEST

@login_manager.user_loader
def load_user(user_id):
    try:
        return User(**usersDL.get_user_by_id(user_id))
    except Exception:
        return None

class Auth(object):
    SECRET_KEY = b'\xb14W\x14\xba\xdb\xc2\xd61\xe2\xea*\x1b\x1fWz'
    ADMIN_ID = 0
    
    def __init__(self, app):
        self.__init_login_mngr(app)

    def __init_login_mngr(self, app):
        global login_manager
        self.mngr = login_manager
        app.secret_key = self.SECRET_KEY
        self.mngr.init_app(app)
        self.mngr.anonymous_user = AnonUser

class User(UserMixin):
    def __init__(self, name='', passwd='', admin=None, _id=None):
        self._id = _id
        self.name = name
        self.passwd = passwd
        self.admin = admin
        
    @property
    def perm(self):
        return Perms.ADMIN if self.admin else Perms.USER

    def get_id(self):
        self._id

#     @property
#     def is_authenticated(self):
#         pass # return usersDL.get_user(self.name, self.passwd) != None
# 
#     @property
#     def is_active(self):
#         pass
#     
#     @property
#     def is_anonymous(self):
#         pass
#     

### user locks TBD
# class Users(object):
#     def __init__(self, users=None):
#         self.users = users or []
#     
#     def who_locks(self, obj):
#         for u in self.users:
#             if obj in [l.pick_obj() for l in self.users.locked_objs]:
#                 return u.name
#         return None
# 
#     def get_user(self, name, passwd=None):
#         for u in self.users:
#             if u.name == name:
#                 if (not passwd) or u.passwd == passwd:
#                     return u
#         return None