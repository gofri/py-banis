#!/usr/bin/python3.6
# encoding: utf-8

from flask import Flask, request
from Mgmt.Pages.home import Home

from Mgmt.auth import Perms, Auth
from Mgmt.Pages.login import LoginPage
from Mgmt.Pages.admin_panel import AdminPanel
from Mgmt.Pages.admin_items import AdminItems


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return Home(Perms.GUEST).html()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return LoginPage(request).html()

@app.route('/admin_panel')
def admin_panel():
    return AdminPanel().html()

@app.route('/admin_items')
def admin_items():
    return AdminItems().html()

if __name__ == "__main__":
    auth = Auth(app)
    app.run(debug=True, use_reloader=False)
