# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for
from stravafollowsync.controller import *
from stravafollowsync.model import *

def print_settings(config):
    print('===================================================================')
    print('settings')
    print('===================================================================')
    for key, value in config:
        print('%s=%s' % (key, value))
    print('===================================================================')

def create_app():
    sfc_app = Flask(__name__, instance_relative_config=True)

    sfc_app.config.from_pyfile('config.cfg', silent=True)
    print_settings(sfc_app.config.items())

    from stravafollowsync.stravafollowsync_blueprint import stravafollowsync
    sfc_app.register_blueprint(stravafollowsync)

    return sfc_app