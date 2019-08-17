#!/usr/bin/python3.6
# encoding: utf-8
import flask

users = [{'_id': 0, 'name':'avner', 'passwd':'papabani', 'admin':True},
         {'_id': 1, 'name':'omri', 'passwd':'kidbani', 'admin':True},
         {'_id': 2, 'name':'omrimor', 'passwd':'badboy', 'admin':False},]

def get_user(name, passwd=''):
    for u in users:
        if u['name'] == name and (not passwd or passwd == u['passwd']):
            return u
    else:
        flask.flash('no such user or bad password')
        return None
    
def get_user_by_id(user_id):
    try:
        return users[user_id] # id == index
    except Exception:
        return None