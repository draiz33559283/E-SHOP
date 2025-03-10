from flask import Flask
from flask_cors import CORS
import os

def create_app(config_name):
    # Get absolute path to static folder
    static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../static'))
    app = Flask(__name__, static_folder=static_path)
    
    # Debug static folder path
    print(f"Static folder path: {app.static_folder}")
    
    # Load configuration
    config_class = getattr(__import__('app.config', fromlist=[f"{config_name.capitalize()}Config"]), 
                         f"{config_name.capitalize()}Config")
    app.config.from_object(config_class)
    
    # Enable debug mode if in development
    if config_name == 'development':
        app.debug = True
    
    # Enable CORS
    CORS(app)
    
    # Register blueprints
    from app.modules.main.route import main_bp
    app.register_blueprint(main_bp)
    
    return app
