#!/usr/bin/python

from application import app

if __name__ == '__main__':
    """
    Main function. Runs the development server
    """
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)
