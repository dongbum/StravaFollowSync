# -*- coding: utf-8 -*-

from flask import render_template
from stravafollowsync.stravafollowsync_blueprint import stravafollowsync

@stravafollowsync.route('/')
def index():
    return render_template('index.html')