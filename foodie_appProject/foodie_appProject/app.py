from flask import Flask
from foodie_appProject.config import Config
from foodie_appProject.extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from foodie_appProject.routes import api_bp
    app.register_blueprint(api_bp)

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
