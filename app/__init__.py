from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from app.config import config
import os

ma = Marshmallow()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    config_name = os.getenv('FLASK_ENV')
    app = Flask(__name__)
    
    app.config['JWT_SECRET_KEY'] = 'super-secret'
    jwt = JWTManager(app)
    
    f = config.factory(config_name if config_name else 'development')
    app.config.from_object(f)
    
    ma.init_app(app)
    f.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.resources import home, user, instructor
    from app.resources.auth_user import auth_user
    from app.resources.auth_instructor import auth_instructor
    app.register_blueprint(home, url_prefix='/home')
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(instructor, url_prefix='/instructor')
    app.register_blueprint(auth_user, url_prefix='/auth_user')
    app.register_blueprint(auth_instructor, url_prefix='/auth_instructor')
    
    
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}
    
    return app
