from pathlib import Path
import os

basedir = os.path.abspath(Path(__file__).parents[2])


class Config(object):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
        
class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_RECORD_QUERIES = False
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

def factory(app):
    configuration = {
        'development': DevelopmentConfig,
        'production': ProductionConfig
    }
    
    return configuration[app];