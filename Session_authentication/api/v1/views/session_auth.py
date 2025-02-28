#!/usr/bin/env python3
""" Session authentification
"""

import os
from flask import abort, jsonify, request

from models.user import User
from api.v1.views import app_views


@app_views.route('auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ Handles user login using session authentification"""

    from api.v1.app import auth

    email = request.form.get("email")
    password = request.form.get("password")

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})
    if not user or len(user) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user_one = user[0]

    if not user_one.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user_one.id)

    response = jsonify(user_one.to_json())

    session_name = os.getenv("SESSION_NAME", "my_session_id")
    response.set_cookie(session_name, session_id)

    return response


@app_views.route(
        'auth_session/logout',
        methods=['DELETE'],
        strict_slashes=False
        )
def logout():
    """Handles user logout (session destruction)"""

    from api.v1.app import auth

    if not auth.destroy_session(request):
        abort(404)

    return jsonify({}), 200
