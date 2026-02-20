from flask import Blueprint, request, jsonify
from foodie_appProject.extensions import db
from foodie_appProject.models import Restaurant, Dish, User, Order, Rating


api_bp = Blueprint("api", __name__, url_prefix="/api/v1")

# ---------------- RESTAURANT ----------------

@api_bp.route("/restaurants", methods=["POST"])
def register_restaurant():
    data = request.json
    if Restaurant.query.filter_by(name=data["name"]).first():
        return {"error": "Restaurant already exists"}, 409

    restaurant = Restaurant(**data)
    db.session.add(restaurant)
    db.session.commit()
    return jsonify({"id": restaurant.id, "name": restaurant.name}), 201


@api_bp.route("/restaurants/<int:id>", methods=["GET"])
def view_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return {"error": "Not found"}, 404

    return jsonify({
        "id": restaurant.id,
        "name": restaurant.name,
        "category": restaurant.category,
        "location": restaurant.location,
        "active": restaurant.active
    })


@api_bp.route("/restaurants/<int:id>/disable", methods=["PUT"])
def disable_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return {"error": "Not found"}, 404

    restaurant.active = False
    db.session.commit()
    return {"message": "Restaurant disabled"}

# ---------------- DISH ----------------

@api_bp.route("/restaurants/<int:rid>/dishes", methods=["POST"])
def add_dish(rid):
    dish = Dish(**request.json, restaurant_id=rid)
    db.session.add(dish)
    db.session.commit()
    return {"dish_id": dish.id}, 201

@api_bp.route("/dishes/<int:dish_id>", methods=["GET"])
def get_dish(dish_id):
    dish = Dish.query.get(dish_id)
    if not dish:
        return {"error": "Dish not found"}, 404

    return {
        "id": dish.id,
        "name": dish.name,
        "price": dish.price,
        "enabled": dish.enabled,
        "restaurant_id": dish.restaurant_id
    }, 200

@api_bp.route("/dishes/<int:id>/status", methods=["PUT"])
def update_dish_status(id):
    dish = Dish.query.get(id)
    if not dish:
        return {"error": "Not found"}, 404

    dish.enabled = request.json["enabled"]
    db.session.commit()
    return {"message": "Dish status updated"}


@api_bp.route("/dishes/<int:id>", methods=["DELETE"])
def delete_dish(id):
    dish = Dish.query.get(id)
    if not dish:
        return {"error": "Not found"}, 404

    db.session.delete(dish)
    db.session.commit()
    return {"message": "Dish deleted"}

# ---------------- USER ----------------

@api_bp.route("/users/register", methods=["POST"])
def register_user():
    data = request.json
    if User.query.filter_by(email=data["email"]).first():
        return {"error": "User already exists"}, 409

    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return {"user_id": user.id}, 201

# ---------------- ORDER ----------------

@api_bp.route("/orders", methods=["POST"])
def place_order():
    order = Order(**request.json)
    db.session.add(order)
    db.session.commit()
    return {"order_id": order.id}, 201

@api_bp.route("/users/<int:user_id>/orders", methods=["GET"])
def get_orders_by_user(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()

    return [
        {
            "order_id": o.id,
            "user_id": o.user_id,
            "restaurant_id": o.restaurant_id,
            "status": o.status
        }
        for o in orders
    ], 200

# ---------------- RATING ----------------

@api_bp.route("/ratings", methods=["POST"])
def give_rating():
    rating = Rating(**request.json)
    db.session.add(rating)
    db.session.commit()
    return {"rating_id": rating.id}, 201

@api_bp.route("/restaurants", methods=["GET"])
def get_all_restaurants():
    restaurants = Restaurant.query.all()

    result = []
    for r in restaurants:
        result.append({
            "id": r.id,
            "name": r.name,
            "category": r.category,
            "location": r.location,
            "active": r.active
        })

    return result, 200


# ---------------- ADMIN ----------------

@api_bp.route("/admin/orders", methods=["GET"])
def view_orders():
    orders = Order.query.all()
    return jsonify([
        {"id": o.id, "user_id": o.user_id, "status": o.status}
        for o in orders
    ])

@api_bp.route("/admin/restaurants/<int:restaurant_id>/approve", methods=["PUT"])
def approve_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        return {"error": "Restaurant not found"}, 404

    restaurant.active = True
    db.session.commit()
    return {"message": "Restaurant approved"}, 200
@api_bp.route("/admin/users/<int:user_id>/orders", methods=["GET"])
def admin_view_orders_by_user(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()

    return [
        {
            "order_id": o.id,
            "restaurant_id": o.restaurant_id,
            "status": o.status
        }
        for o in orders
    ], 200

@api_bp.route("/admin/feedback", methods=["GET"])
def admin_view_feedback():
    feedbacks = Rating.query.all()

    return [
        {
            "rating_id": f.id,
            "order_id": f.order_id,
            "rating": f.rating,
            "comment": f.comment
        }
        for f in feedbacks
    ], 200
