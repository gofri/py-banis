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
    return Home(Perms.GUEST).html()

@app.route('/login')
def login():
    return Login(Perms.GUEST).html()

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
