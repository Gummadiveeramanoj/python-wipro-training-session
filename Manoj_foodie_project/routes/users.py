from flask import Blueprint, request, jsonify
from uuid import uuid4
from data_store import users

user_bp = Blueprint("users", __name__)


@user_bp.route("/api/v1/users/register", methods=["POST"])
def register_user():
    data = request.json
    for u in users.values():
        if u["email"] == data.get("email"):
            return jsonify({"message": "User already exists"}), 409

    uid = str(uuid4())
    users[uid] = {
        "id": uid,
        "name": data.get("name"),
        "email": data.get("email"),
    }
    return jsonify(users[uid]), 201
