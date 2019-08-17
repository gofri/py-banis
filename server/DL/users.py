#!/usr/bin/python3.6
# encoding: utf-8
import flask

users = [{'name':'avner', 'passwd':'papabani', 'admin':True},
         {'name':'omri', 'passwd':'kidbani', 'admin':True},
         {'name':'omrimor', 'passwd':'badboy', 'admin':False},]

def get_user(name, passwd=''):
    global users
    for u in users:
        if u['name'] == name and (not passwd or passwd == u['passwd']):
            return u
    else:
        flask.flash('no such user or bad password')
        return None
    
def get_user_by_id(user_id):
    global users
    for u in users:
        if u['name'] == user_id:
            return u

    flask.flash("No user found")
    return None