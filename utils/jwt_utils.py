import jwt
import datetime
from dotenv import load_dotenv
import os
from datetime import timezone
from flask import request, jsonify
from functools import wraps

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET", "your_default_secret")
JWT_ALGORITHM = "HS256"

def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.now(timezone.utc) + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token if isinstance(token, str) else token.decode("utf-8")


def decode_token(token):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid Authorization header"}), 401

        token = auth_header.split(" ")[1]
        user_id = decode_token(token)

        if not user_id:
            return jsonify({"error": "Invalid or expired token"}), 401

        kwargs["current_user_id"] = user_id
        return func(*args, **kwargs)
    return wrapper