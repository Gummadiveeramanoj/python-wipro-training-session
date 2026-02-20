from flask import Blueprint, request, jsonify
from uuid import uuid4
from data_store import restaurants

restaurant_bp = Blueprint("restaurants", __name__)


@restaurant_bp.route("/api/v1/restaurants", methods=["POST"])
def register_restaurant():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"message": "Invalid data"}), 400

    for r in restaurants.values():
        if r["name"] == data["name"]:
            return jsonify({"message": "Restaurant already exists"}), 409

    rid = str(uuid4())
    restaurants[rid] = {
        "id": rid,
        "name": data["name"],
        "category": data.get("category"),
        "location": data.get("location"),
        "enabled": True,
        "approved": False,
    }
    return jsonify(restaurants[rid]), 201


@restaurant_bp.route("/api/v1/restaurants/<rid>", methods=["GET"])
def view_restaurant(rid):
    if rid not in restaurants:
        return jsonify({"message": "Restaurant not found"}), 404
    return jsonify(restaurants[rid]), 200


@restaurant_bp.route("/api/v1/restaurants/<rid>", methods=["PUT"])
def update_restaurant(rid):
    if rid not in restaurants:
        return jsonify({"message": "Restaurant not found"}), 404
    restaurants[rid].update(request.json)
    return jsonify(restaurants[rid]), 200


@restaurant_bp.route("/api/v1/restaurants/<rid>/disable", methods=["PUT"])
def disable_restaurant(rid):
    if rid not in restaurants:
        return jsonify({"message": "Restaurant not found"}), 404
    restaurants[rid]["enabled"] = False
    return jsonify({"message": "Restaurant disabled"}), 200
