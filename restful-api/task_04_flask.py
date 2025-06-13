#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store for users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Route for the root URL
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Route to get the list of all users' usernames
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

# Route to get the status of the server
@app.route("/status")
def status():
    return "OK"

# Route to get user details by username
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route to add a new user using POST request
@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()

    # Check if username is provided
    if "username" not in user_data:
        return jsonify({"error": "Username is required"}), 400

    # Check if other required fields are provided
    if "name" not in user_data or "age" not in user_data or "city" not in user_data:
        return jsonify({"error": "Name, age, and city are required"}), 400

    username = user_data["username"]

    # Check if user already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    # Add the new user to the dictionary
    users[username] = {
        "username": username,
        "name": user_data["name"],
        "age": user_data["age"],
        "city": user_data["city"]
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
