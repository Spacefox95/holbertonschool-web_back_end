#!/usr/bin/env python3


from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	title = {'title' : 'Welcome to Holberton'}
	h1 = {'h1' : 'Hello World'}
	return '''<html>
    <head>
        <title>title['title']</title>
    </head>
    <body>
        <h1>h1['h1']</h1>
    </body>
</html>'''