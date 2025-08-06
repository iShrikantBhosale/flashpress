from flask import Flask
from app.config import config_map
from app.extensions import init_extensions

def create_app(config_name="development"):
    """Application factory for FlashPress"""
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(config_map[config_name])

    # Initialize extensions
    init_extensions(app)

    # Register blueprints
    from app.public.routes import public_bp
    app.register_blueprint(public_bp)

    return app
