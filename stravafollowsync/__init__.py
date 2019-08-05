# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for
from stravafollowsync.controller import *
from stravafollowsync.model import *

def create_app():
    sfc_app = Flask(__name__)

    from stravafollowsync.stravafollowsync_blueprint import stravafollowsync
    sfc_app.register_blueprint(stravafollowsync)

    return sfc_app