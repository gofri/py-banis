#!/usr/bin/python3.6
# encoding: utf-8

from functools import wraps
from flask_login import current_user
from flask import flash, redirect, url_for

def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if current_user.admin:
            return f(*args, **kwargs)
        else:
            flash("You need to be an admin to view this page.")
            return redirect(url_for('index'))
    return wrap