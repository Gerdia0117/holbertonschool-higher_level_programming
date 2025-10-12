#!/usr/bin/python3
"""
Flask API
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
users = {}


@app.route('/', strict_slashes=False)
def home():
    """Root route"""
    return "Welcome to the Flask API!"


@app.route('/status', strict_slashes=False)
def status():
    """Returns API status"""
    return "OK"


@app.route('/data', strict_slashes=False)
def get_data():
    """Return list of usernames"""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/users/<username>', strict_slashes=False)
def get_user(username):
    """Return a user object by username"""
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route('/add_user', methods=['POST'], strict_slashes=False)
def add_user():
    """Add a new user"""
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()