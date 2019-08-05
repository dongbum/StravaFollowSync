# -*- coding: utf-8 -*-

from flask import Blueprint

stravafollowsync = Blueprint('stravafollowsync', __name__, template_folder='../templates', static_folder='../static')