from flask import Flask # noqA
from .extensions import socketio, cors
from .config import Config
from ..storage import Database

DB = Database()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    cors.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*", async_mode='gevent')

    @app.route('/')
    def root():
        return 'I am root'

    with app.app_context():
        from .. import routes  # noqA

    return app


