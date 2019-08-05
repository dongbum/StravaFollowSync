# -*- coding: utf-8 -*-

from flask import render_template
from stravafollowsync.stravafollowsync_blueprint import stravafollowsync

@stravafollowsync.route('/test')
def test():
    return render_template('test.html')