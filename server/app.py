#!/usr/bin/python3.6
# encoding: utf-8

from flask import Flask, request
from Mgmt.Pages.index import HomePage

from Mgmt.auth import Perms, Auth
from Mgmt.Pages.login import LoginPage
from Mgmt.Pages.admin_panel import AdminPanel
from Mgmt.Pages.admin_items import AdminItems
from flask_login.utils import login_required, current_user
from flask_login.login_manager import LoginManager
from Mgmt.utils import admin_required

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return HomePage(request).html()

@app.route('/login', methods=['GET', 'POST'])
def login():
    return LoginPage(request, app).html()

@app.route('/admin_panel')
@admin_required
def admin_panel():
    return AdminPanel().html()

@app.route('/admin_items')
@admin_required
def admin_items():
    return AdminItems().html()

login_mngr  = LoginManager()

@login_mngr.user_loader
def load_user(user_id):
    return Auth().load_user(user_id)

if __name__ == "__main__":
    auth = Auth(app, login_mngr)
    app.run(debug=True, use_reloader=False)
