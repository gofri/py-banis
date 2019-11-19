 #!/usr/bin/python3.6
# encoding: utf-8
import flask

class UsersDL(object):
    def __init__(self):
        self._users = None

        self._load_users()
    
    def _load_users(self):
        self._users = [{'name':'avner', 'passwd':'papabani', 'admin':True},
                       {'name':'omri', 'passwd':'kidbani', 'admin':True},
                       {'name':'omrimor', 'passwd':'badboy', 'admin':False},]
    
    def add_user(self, name, passwd, admin):
        if self.get_user(name):
            flask.flash('user already exist')
        else:
            self._users.append({'name':name, 'passwd':passwd, 'admin':admin})
    
    def get_user(self, name, passwd=''):
        for u in self._users:
            if u['name'] == name and (not passwd or passwd == u['passwd']):
                return u
        else:
            flask.flash('no such user or bad password')
            return None
        
    def get_user_by_id(self, user_id):
        for u in self._users:
            if u['name'] == user_id:
                return u
    
        flask.flash("No user found")
        return None
