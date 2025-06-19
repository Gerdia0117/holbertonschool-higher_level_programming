#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store for user (renamed from 'users' for clarity)
user = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Home route
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Return all usernames
@app.route("/data")
def get_data():
    return jsonify(list(user.keys()))

# Return API status
@app.route("/status")
def status():
    return "OK"

# Get user data by username
@app.route("/users/<username>")
def get_user(username):
    user_data = user.get(username)
    if user_data:
        return jsonify(user_data)
    else:
        return jsonify({"error": "User not found"}), 404

# Add new user via POST
@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()

    # Field validations with specific error messages
    if not user_data:
        return jsonify({"error": "No JSON data provided"}), 400

    if "username" not in user_data:
        return jsonify({"error": "Missing username"}), 400

    if "name" not in user_data:
        return jsonify({"error": "Missing name"}), 400

    if "age" not in user_data:
        return jsonify({"error": "Missing age"}), 400

    if "city" not in user_data:
        return jsonify({"error": "Missing city"}), 400

    username = user_data["username"]

    # Check for existing user
    if username in user:
        return jsonify({"error": "Username already exists"}), 400

    # Add new user
    user[username] = {
        "username": username,
        "name": user_data["name"],
        "age": user_data["age"],
        "city": user_data["city"]
    }

    return jsonify({
        "message": "User added",
        "user": user[username]
    }), 201

# Correct main entry point
if __name__ == "__main__":
    app.run(debug=True, port=5001)
