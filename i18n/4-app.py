#!/usr/bin/env python3
""" Flask server setup"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """ Class to configure babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_locale():
    """ use the locale from the user setttings"""
    if "locale" in request.args and request.args['locale'] in Config.LANGUAGES:
        return request.args['locale']
    return request.accept_languages.best_match(Config.LANGUAGES)


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """ Return to the main page"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
