#build app brains
from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

#from flask_login import LoginManager





db = SQLAlchemy()
# login_manager = LoginManager()
# login_manager.session_protection='strong'
# login_manager.login_view='main.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    
    #initialize extensions
    db.init_app(app)
    # login_manager.init_app(app)
    
    
    # registering main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    
    
    #  # setting config
    # from .requests import configure_request
    # configure_request(app)
    return app