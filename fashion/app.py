from flask import Flask

from fashion.routes import create_routes


def create_app(debug=False):
    app = Flask(__name__)
    create_routes(app)
    return app
