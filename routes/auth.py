from flask import Blueprint, request, jsonify
from utils.validators import LoginSchema
from utils.security import verify_password
from utils.jwt_utils import generate_token
from db import get_db
from pydantic import ValidationError
from utils.jwt_utils import require_auth

auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        validated = LoginSchema(**data)
    except (ValidationError, TypeError) as e:
        return jsonify({"error": str(e)}), 400

    db = get_db()
    user = db.execute("SELECT * FROM users WHERE email = ?", 
                      (validated.email,)).fetchone()

    if user and verify_password(validated.password, user["password"]):
        token = generate_token(user["id"])
        return jsonify({"status": "success", "token": token}), 200
    return jsonify({"status": "failed"}), 401


@auth_bp.route('/me', methods=['GET'])
@require_auth
def get_current_user(user_id):
    db = get_db()
    user = db.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,)).fetchone()
    if user:
        return jsonify(dict(user)), 200
    return jsonify({"error": "User not found"}), 404
