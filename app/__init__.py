from flask import Flask
from flask_migrate import Migrate
# from flask_login import LoginManager
# from config import app_config
from .extensions import db
from .routes import short

# login_manager = LoginManager()

def create_app(config_name):
    """ 
    https://stackoverflow.com/questions/20744277/sqlalchemy-create-all-does-not-create-tables
    """
    app = Flask(__name__, instance_relative_config=True)
    #app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # migrate = Migrate(app, db)
    app.register_blueprint(short)

    from app import models
    with app.app_context():
        db.create_all()
        db.session.commit()

    return app
