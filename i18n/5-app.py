#!/usr/bin/env python3
""" Flask server setup"""


from flask import Flask, g, render_template, request
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user():
    """ Retrieve user information from login_as parameter"""
    user_id = request.args.get('login_as')
    if user_id and user_id in users:
        return users.get(user_id)
    return None


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
babel.init_app(app, locale_selector=get_locale)


@app.before_request
def before_request():
    """Set user as global in Flask g"""
    g.user = get_user()


@app.route('/')
def index():
    """ Return to the main page"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
