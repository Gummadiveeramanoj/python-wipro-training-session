from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# ---------------- In-Memory Data ----------------
restaurants = {}
dishes = {}
users = {}
orders = {}
feedback = []

# ---------------- Restaurant APIs ----------------
@app.route("/api/v1/restaurants", methods=["POST"])
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
        "approved": False
    }
    return jsonify(restaurants[rid]), 201


@app.route("/api/v1/restaurants/<rid>", methods=["GET"])
def view_restaurant(rid):
    if rid not in restaurants:
        return jsonify({"message": "Restaurant not found"}), 404
    return jsonify(restaurants[rid]), 200


@app.route("/api/v1/restaurants/<rid>", methods=["PUT"])
def update_restaurant(rid):
    if rid not in restaurants:
        return jsonify({"message": "Restaurant not found"}), 404
    restaurants[rid].update(request.json)
    return jsonify(restaurants[rid]), 200


@app.route("/api/v1/restaurants/<rid>/disable", methods=["PUT"])
def disable_restaurant(rid):
    if rid not in restaurants:
        return jsonify({"message": "Restaurant not found"}), 404
    restaurants[rid]["enabled"] = False
    return jsonify({"message": "Restaurant disabled"}), 200

# ---------------- Dish APIs ----------------
@app.route("/api/v1/restaurants/<rid>/dishes", methods=["POST"])
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
        "enabled": True
    }
    return jsonify(dishes[did]), 201


@app.route("/api/v1/dishes/<did>", methods=["PUT"])
def update_dish(did):
    if did not in dishes:
        return jsonify({"message": "Dish not found"}), 404
    dishes[did].update(request.json)
    return jsonify(dishes[did]), 200


@app.route("/api/v1/dishes/<did>/status", methods=["PUT"])
def dish_status(did):
    if did not in dishes:
        return jsonify({"message": "Dish not found"}), 404
    dishes[did]["enabled"] = request.json.get("enabled")
    return jsonify({"message": "Dish status updated"}), 200


@app.route("/api/v1/dishes/<did>", methods=["DELETE"])
def delete_dish(did):
    if did not in dishes:
        return jsonify({"message": "Dish not found"}), 404
    del dishes[did]
    return jsonify({"message": "Dish deleted"}), 200

# ---------------- User APIs ----------------
@app.route("/api/v1/users/register", methods=["POST"])
def register_user():
    data = request.json
    for u in users.values():
        if u["email"] == data.get("email"):
            return jsonify({"message": "User already exists"}), 409

    uid = str(uuid4())
    users[uid] = {
        "id": uid,
        "name": data.get("name"),
        "email": data.get("email")
    }
    return jsonify(users[uid]), 201

# ---------------- Order APIs ----------------
@app.route("/api/v1/orders", methods=["POST"])
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
        "status": "PLACED"
    }
    return jsonify(orders[oid]), 201

# ---------------- Admin APIs ----------------
@app.route("/api/v1/admin/restaurants/<rid>/approve", methods=["PUT"])
def approve_restaurant(rid):
    if rid not in restaurants:
        return jsonify({"message": "Restaurant not found"}), 404
    restaurants[rid]["approved"] = True
    return jsonify({"message": "Restaurant approved"}), 200


@app.route("/api/v1/admin/orders", methods=["GET"])
def view_orders():
    return jsonify(list(orders.values())), 200


@app.route("/api/v1/admin/feedback", methods=["GET"])
def view_feedback():
    return jsonify(feedback), 200


if __name__ == "__main__":
    app.run(debug=True)
