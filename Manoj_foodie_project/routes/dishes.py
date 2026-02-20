from flask import Blueprint, request, jsonify
from uuid import uuid4
from data_store import restaurants, dishes

dish_bp = Blueprint("dishes", __name__)


@dish_bp.route("/api/v1/restaurants/<rid>/dishes", methods=["POST"])
def add_dish(rid):
    if rid not in restaurants:
        return jsonify({"message": "Restaurant not found"}), 404

    data = request.json
    did = str(uuid4())
    dishes[did] = {
        "id": did,
        "restaurant_id": rid,
        "name": data.get("name"),
        "price": data.get("price"),
        "enabled": True,
    }
    return jsonify(dishes[did]), 201


@dish_bp.route("/api/v1/dishes/<did>", methods=["PUT"])
def update_dish(did):
    if did not in dishes:
        return jsonify({"message": "Dish not found"}), 404
    dishes[did].update(request.json)
    return jsonify(dishes[did]), 200


@dish_bp.route("/api/v1/dishes/<did>/status", methods=["PUT"])
def dish_status(did):
    if did not in dishes:
        return jsonify({"message": "Dish not found"}), 404
    dishes[did]["enabled"] = request.json.get("enabled")
    return jsonify({"message": "Dish status updated"}), 200


@dish_bp.route("/api/v1/dishes/<did>", methods=["DELETE"])
def delete_dish(did):
    if did not in dishes:
        return jsonify({"message": "Dish not found"}), 404
    del dishes[did]
    return jsonify({"message": "Dish deleted"}), 200
