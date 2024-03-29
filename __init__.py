from flask import flask

from .extensions import mongo

def create_app():
    app = Flask(__name__)

    mongo.init_app(app)

    return app