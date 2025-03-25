#!/usr/bin/env python3
""" Flask server setup"""


from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """ Return to the main page"""

    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
