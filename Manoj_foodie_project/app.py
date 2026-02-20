from flask import Flask
from routes.restaurants import restaurant_bp
from routes.dishes import dish_bp
from routes.users import user_bp
from routes.orders import order_bp
from routes.admin import admin_bp

app = Flask(__name__)

# Register all Blueprints
app.register_blueprint(restaurant_bp)
app.register_blueprint(dish_bp)
app.register_blueprint(user_bp)
app.register_blueprint(order_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)
