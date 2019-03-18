import os
class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI ="mysql+pymysql://root:rootroot@127.0.0.1/gcloudtest"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "random string"

class ProductionConfig(Config):
    DEBUG = False
    ENV = "production"

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"
class TestingConfig(Config):
    TESTING = True
    ENV = "testing"
