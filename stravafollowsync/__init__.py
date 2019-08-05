# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for

def create_app():
    strava_follow_sync = Flask(__name__)

    return strava_follow_sync