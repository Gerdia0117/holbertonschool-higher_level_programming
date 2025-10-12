#!/usr/bin/python3
"""
Flask API, Basic Auth and JWT Authentication
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# In-memory user data
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# ---------------- Basic Authentication ---------------- #

@auth.verify_password
def verify_password(username, password):
    """Verify username and password"""
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return None
    return user


@app.route('/basic-protected', strict_slashes=False)
@auth.login_required
def basic_protected():
    """Route protected by Basic Auth"""
    return "Basic Auth: Access Granted"


# ---------------- JWT Authentication ---------------- #

@app.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """Login route for JWT"""
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing credentials"}), 401

    username = data["username"]
    password = data["password"]
    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity={
        "username": username,
        "role": user["role"]
    })
    return jsonify({"access_token": token}), 200


@app.route('/jwt-protected', strict_slashes=False)
@jwt_required()
def jwt_protected():
    """Protected route with JWT"""
    return "JWT Auth: Access Granted"


@app.route('/admin-only', strict_slashes=False)
@jwt_required()
def admin_only():
    """Admin-only route"""
    user = get_jwt_identity()
    if user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# ---------------- Error Handling ---------------- #

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
