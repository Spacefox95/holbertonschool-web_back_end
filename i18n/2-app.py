#!/usr/bin/env python3
""" Flask server setup"""


from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """ Class to configure babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_locale():
    """ use the locale from the user setttings"""
    return request.accept_languages.best_match(Config.LANGUAGES)


babel.init_app(app, locale_selector=get_locale())


@app.route('/')
def index():
    """ Return to the main page"""

    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
