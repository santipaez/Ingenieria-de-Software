from app.config.config import DevelopmentConfig, ProductionConfig, factory

def test_development_config():
    config = DevelopmentConfig()
    assert config.TESTING == True
    assert config.DEBUG == True
    assert config.FLASK_ENV == 'development'
    assert config.SQLALCHEMY_TRACK_MODIFICATIONS == True

def test_production_config():
    config = ProductionConfig()
    assert config.TESTING == False
    assert config.DEBUG == False
    assert config.FLASK_ENV == 'production'
    assert config.SQLALCHEMY_RECORD_QUERIES == False

def test_factory():
    assert factory('development') == DevelopmentConfig
    assert factory('production') == ProductionConfig