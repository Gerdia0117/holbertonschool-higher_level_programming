#!/usr/bin/python3
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)
import datetime

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change this in production!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=1)
jwt = JWTManager(app)
basic_auth = HTTPBasicAuth()

# In-memory user storage
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

@basic_auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username

@basic_auth.error_handler
def basic_auth_error(status):
    return jsonify({"error": "Missing or invalid credentials"}), status

@app.route('/')
def home():
    return "Welcome to the Flask API with Security!"

# Basic Authentication Protected Route
@app.route('/basic-protected')
@basic_auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# JWT Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if username not in users or not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Invalid username or password"}), 401

    # Include user role in the JWT identity
    additional_claims = {"role": users[username]['role']}
    access_token = create_access_token(
        identity=username,
        additional_claims=additional_claims
    )
    return jsonify(access_token=access_token)

# JWT Protected Route
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# Admin-only Route
@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    user_role = get_jwt().get('role', None)

    if user_role != 'admin':
        return jsonify({"error": "Missing admin privileges"}), 403

    return "Admin Access: Granted"

# JWT Error Handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token format"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Missing valid token (expired)"}), 401

if __name__ == '__main__':
    app.run(debug=True)
