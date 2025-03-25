#!/usr/bin/env python3
""" Flask server setup"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ Return to the main page"""
    title = "Welcome to Holberton"
    h1 = 'Hello world'

    return render_template('0-index.html',
                           title=title,
                           h1=h1)
