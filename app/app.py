from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application


def register_extensions(application):
    db.init_app(application)
    api = Api(application)




if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run()
