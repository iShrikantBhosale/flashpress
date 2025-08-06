from flask import Flask

def create_app():
    """Application factory for FlashPress"""
    app = Flask(__name__)

    # Import and register public blueprint
    from app.public.routes import public_bp
    app.register_blueprint(public_bp)

    return app
