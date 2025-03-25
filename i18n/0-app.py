#!/usr/bin/env python3
""" Flask server setup"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ Return to the main page"""
    return render_template('./templates/0-index.html')
