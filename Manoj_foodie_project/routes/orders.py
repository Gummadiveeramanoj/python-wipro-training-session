from flask import Blueprint, request, jsonify
from uuid import uuid4
from data_store import orders

order_bp = Blueprint("orders", __name__)


@order_bp.route("/api/v1/orders", methods=["POST"])
def place_order():
    data = request.json
    if not data:
        return jsonify({"message": "Invalid order data"}), 400

    oid = str(uuid4())
    orders[oid] = {
        "id": oid,
        "user_id": data.get("user_id"),
        "restaurant_id": data.get("restaurant_id"),
        "dishes": data.get("dishes"),
        "status": "PLACED",
    }
    return jsonify(orders[oid]), 201
