#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time     : 2020/3/18 12:38
# @Author   : Jiahai Liu
# @Email    : liujiahai@szkingdom.com
# @File     : hello.py
from flask import Flask, url_for, request, render_template
from markupsafe import escape


app = Flask(__name__)


# @app.route('/')
# def index():
#     return 'Index Page'
#
#
# @app.route('/hello')
# def hello():
#     return 'Hello, World'
#
#
# @app.route('/login')
# def login():
#     return 'login'
#
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % escape(username)
#
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id
#
#
# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % escape(subpath)
#
#
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('show_user_profile', username='John Doe'))
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

# rendering templates
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)