from flask import Blueprint, request, jsonify
from db import get_db, dict_from_row
from utils.validators import UserCreateSchema,UserUpdateSchema
from pydantic import ValidationError
from utils.security import hash_password
from utils.jwt_utils import require_auth


users_bp = Blueprint('users', __name__)


@users_bp.route('/users', methods=['GET'])
@require_auth
def get_all_users(current_user_id):
    db = get_db()
    users = db.execute("SELECT * FROM users").fetchall()
    return jsonify([dict_from_row(u) for u in users]), 200

@users_bp.route('/user/<user_id>', methods=['GET'])
@require_auth
def get_user(user_id,current_user_id):
    db = get_db()
    user = db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    if user:
        return jsonify(dict_from_row(user)), 200
    return jsonify({"error": "User not found"}), 404


@users_bp.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        validated = UserCreateSchema(**data)
    except (ValidationError, TypeError) as e:
        return jsonify({"error": str(e)}), 400

    hashed_pw = hash_password(validated.password)

    db = get_db()
    db.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
               (validated.name, validated.email, hashed_pw))
    db.commit()
    return jsonify({"message": "User created"}), 201


@users_bp.route('/user/<user_id>', methods=['PUT'])
@require_auth
def update_user(user_id,current_user_id):
    try:
        data = request.get_json()
        validated = UserUpdateSchema(**data)
    except (ValidationError, TypeError) as e:
        return jsonify({"error": str(e)}), 400

    db = get_db()
    db.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", 
               (validated.name, validated.email, user_id))
    db.commit()
    return jsonify({"message": "User updated"}), 200

@users_bp.route('/user/<user_id>', methods=['DELETE'])
@require_auth
def delete_user(user_id,current_user_id):
    db = get_db()
    db.execute("DELETE FROM users WHERE id = ?", (user_id,))
    db.commit()
    return jsonify({"message": f"User {user_id} deleted"}), 200

@users_bp.route('/search', methods=['GET'])
def search_users():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Please provide a name to search"}), 400

    db = get_db()
    users = db.execute("SELECT * FROM users WHERE name LIKE ?", (f"%{name}%",)).fetchall()
    return jsonify([dict_from_row(u) for u in users]), 200
