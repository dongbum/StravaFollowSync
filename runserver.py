# -*- coding: utf-8 -*-

from stravafollowsync import create_app

application = create_app()

if __name__ == '__main__':
    print("starting test server...")

    application.run(host='127.0.0.1', port=5000, debug=True)