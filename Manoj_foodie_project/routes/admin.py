from flask import Blueprint, jsonify
from data_store import restaurants, orders, feedback

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/api/v1/admin/restaurants/<rid>/approve", methods=["PUT"])
def approve_restaurant(rid):
    if rid not in restaurants:
        return jsonify({"message": "Restaurant not found"}), 404
    restaurants[rid]["approved"] = True
    return jsonify({"message": "Restaurant approved"}), 200


@admin_bp.route("/api/v1/admin/orders", methods=["GET"])
def view_orders():
    return jsonify(list(orders.values())), 200


@admin_bp.route("/api/v1/admin/feedback", methods=["GET"])
def view_feedback():
    return jsonify(feedback), 200
