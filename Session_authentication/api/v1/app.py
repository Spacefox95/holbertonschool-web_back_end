#!/usr/bin/env python3
"""
Route module for the API
"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = os.getenv("AUTH_TYPE")
if auth_type:
    from api.v1.auth.session_auth import SessionAuth
    from api.v1.auth.auth import Auth
    from api.v1.auth.basic_auth import BasicAuth

    if auth_type == "basic_auth":
        auth = BasicAuth()
    if auth_type == "session_auth":
        auth = SessionAuth()
    else:
        auth = Auth()


@app.before_request
def load_user():
    """Load the user authorization"""
    excluded_path = [
        "/api/v1/status/",
        "/api/v1/unauthorized/",
        "/api/v1/forbidden/",
        "/api/v1/auth_session/login/"
    ]
    if auth is None:
        return
    if request.path in excluded_path:
        return
    if not auth.require_auth(request.path, excluded_path):
        return
    if auth.authorization_header(
        request
        ) is None and auth.session_cookie(
            request
            ) is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)
    request.current_user = auth.current_user(request)


@app.errorhandler(404)
def not_found(error) -> str:
    """Not found handler"""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(403)
def forbidden(error) -> str:
    """Not allowed"""
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(401)
def not_authorized(error) -> str:
    """Not authorized"""
    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
