#!/usr/bin/python3.6
# encoding: utf-8

from flask import Flask, render_template
from Mgmt.Pages.home import Home

from Mgmt.users import Perms
from Mgmt.Pages.login import Login

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('home.html', **Home(Perms.GUEST).content_dict())

@app.route('/login')
def login():
    return render_template('login.html', **Login(Perms.GUEST).content_dict())

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
