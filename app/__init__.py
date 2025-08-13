
from flask import Flask
from .config import Config
from .routes import register_routes
from flask import jsonify
from flask_cors import CORS



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = Config.sql

    
    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to the Flask app"}), 200
    
    register_routes(app)

    return app




