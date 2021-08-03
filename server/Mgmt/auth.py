#!/usr/bin/python3.6
# encoding: utf-8
from flask_login import LoginManager, current_user
from flask_login.mixins import UserMixin, AnonymousUserMixin
from DL import users as usersDL
import flask_login
from Core.singleton import Singleton

class Perms(object):
    NAMES = ["guest", "user", "admin"]
    GUEST = 0
    USER = 1
    ADMIN = 2

    @classmethod
    def sanity_check(cls, perm):
        assert 0 <= perm < len(Perms.NAMES) 

class AnonUser(AnonymousUserMixin):
    def __init__(self, *args, **kwargs):
        super(*args, **kwargs)
        self.name = 'GUEST'
    
    @property
    def perm(self):
        return Perms.GUEST
    
    @property
    def admin(self):
        return False

class Auth(object, metaclass=Singleton):
    SECRET_KEY = b'\xb14W\x14\xba\xdb\xc2\xd61\xe2\xea*\x1b\x1fWz'
    ADMIN_ID = 0
    
    def __init__(self, app, login_mngr):
        self.__init_login_mngr(app, login_mngr)

    def __init_login_mngr(self, app, login_mngr):
        self.mngr = login_mngr
        self.app = app
        self.app.secret_key = self.SECRET_KEY
        self.app.config['USERS'] = []
        self.mngr.init_app(app)
        self.mngr.anonymous_user = AnonUser
        
    def load_user(self, user_id):
        for u in self.app.config['USERS']:
            if u.name == user_id:
                return u

        return None

# TODO load usersDL into this type
class User(UserMixin):
    def __init__(self, name='', passwd='', admin=None):
        self.name = name
        self.passwd = passwd
        self.admin = admin
        
    @property
    def perm(self):
        return Perms.ADMIN if self.admin else Perms.USER

    def get_id(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

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
