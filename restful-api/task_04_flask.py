#!/usr/bin/python3
"""
A simple Flask-based REST API that manages a dictionary of users
in memory, supporting GET and POST requests.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store users in memory
users = {}


@app.route("/")
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    """Returns a list of all usernames in the dictionary."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Returns the API status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full user object for a given username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Parses incoming JSON to add a new user.
    Handles validation for JSON validity, missing username, and duplicates.
    """
    # Parse incoming JSON
    data = request.get_json(silent=True)

    # Check if JSON is valid
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    # Check if username is present
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user to memory
    users[username] = data

    # Return success with status 201 Created
    response = {
        "message": "User added",
        "user": data
    }
    return jsonify(response), 201


if __name__ == "__main__":
    app.run()
