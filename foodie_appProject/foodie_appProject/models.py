from foodie_appProject.extensions import db


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    category = db.Column(db.String(50))
    location = db.Column(db.String(100))
    active = db.Column(db.Boolean, default=True)


class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    enabled = db.Column(db.Boolean, default=True)
    restaurant_id = db.Column(db.Integer)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer)
    status = db.Column(db.String(50), default="PLACED")


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String(200))
