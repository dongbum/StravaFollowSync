# -*- coding: utf-8 -*-

from flask import render_template, request, url_for, current_app, session
from stravafollowsync.stravafollowsync_blueprint import stravafollowsync
from stravalib import Client

@stravafollowsync.route('/test')
def test():
    client = Client()
    url = client.authorization_url(client_id=current_app.config['STRAVA_CLIENT_ID'],
                                   redirect_uri=url_for('.logged_in', _external=True),
                                   approval_prompt='auto')

    return render_template('test.html', authorize_url=url)

@stravafollowsync.route('/strava_oauth')
def logged_in():
    error = request.args.get('error')
    state = request.args.get('state')

    try:
        if error:
            return render_template('login_error.html', error=error)
        else:
            code = request.args.get('code')

            client = Client()
            access_token = client.exchange_code_for_token(client_id=current_app.config['STRAVA_CLIENT_ID'],
                                                          client_secret=current_app.config['STRAVA_CLIENT_SECRET'],
                                                          code=code)
            strava_athlete = client.get_athlete()

            session.parmanent = True
            session['access_token'] = access_token

        return render_template('login_results.html', athlete=strava_athlete, access_token=access_token)
    except Exception as e:
        return render_template('login_error.html', error=str(e))