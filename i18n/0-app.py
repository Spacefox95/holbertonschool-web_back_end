#!/usr/bin/env python3
""" Flask server setup"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ Return to the main page"""

    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
