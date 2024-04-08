from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config
import os

db = SQLAlchemy()

def create_app():
    config_name = os.getenv('FLASK_ENV')
    app = Flask(__name__)
        
    f = config.factory(config_name if config_name else 'development')
    app.config.from_object(f)
    
    
    f.init_app(app)
    db.init_app(app)
    
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}
    
    return app
