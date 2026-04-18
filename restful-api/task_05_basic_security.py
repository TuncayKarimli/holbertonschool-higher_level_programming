#!/usr/bin/python3
"""
Flask API implementing Basic Auth, JWT, and Role-Based Access Control.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuration
app.config['JWT_SECRET_KEY'] = 'your-very-secret-key'  # Change in production
auth = HTTPBasicAuth()
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


# --- Basic Auth Logic ---

@auth.verify_password
def verify_password(username, password):
    """Verifies credentials for Basic Authentication."""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None


# --- JWT Error Handlers (Required for consistency) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


# --- API Endpoints ---

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Protected by Basic Auth."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Authenticates user and returns a JWT."""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # We store the username and role inside the token identity
        access_token = create_access_token(
            identity={"username": username, "role": user['role']}
        )
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Protected by JWT."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Protected by JWT with specific Role-Based Access Control."""
    current_user = get_jwt_identity()
    
    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
