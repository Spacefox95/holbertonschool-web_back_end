#!/usr/bin/env python3
""" Flask server setup"""


from flask import Flask, g, render_template, request
from flask_babel import Babel
import pytz


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
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    user = get_user()
    if user and user.get("locale") in Config.LANGUAGES:
        return user['locale']
    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user():
    """ Retrieve user information from login_as parameter"""
    if "login_as" in request.args:
        user_id = int(request.args['login_as'])
        return users.get(user_id)
    return None


def get_timezone():
    """ Retrieve the timezone"""

    timezone = request.args.get("timezone")
    try:
        if timezone:
            pytz.timezone(timezone)
            return timezone
        user = get_user()
        if user and user.get('timezone'):
            pytz.timezone(user['timezone'])
            return user['timezone']
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.before_request
def before_request():
    """Set user as global in Flask g"""
    g.user = get_user()


@app.route('/')
def index():
    """ Return to the main page"""
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run()
