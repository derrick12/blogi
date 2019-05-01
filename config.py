import os

class Config:
    '''
    General configuration parent class
    Database URI: db+driver://username:password@host/database. It configures the location of the database, 
    psycopg2 : driver that connects SQLAlchemy with the app
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://derrick:architect@localhost/blogi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Blogi'
    SENDER_EMAIL = 'derrick@moringaschool.com'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    Production  configuration child class
    Active during production 

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class TestConfig(Config):
    '''
    Testing configuration child class
    Active during testing
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://derrick:architect@localhost/blogi_test'

class DevConfig(Config):
    '''
    Development  configuration child class
    Active during development

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://derrick:architect@localhost/blogi'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
#'test':TestConfig
}
