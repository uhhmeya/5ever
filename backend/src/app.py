from . import app, socketio, cors
from .routes import websocket # noqa: F401
import secrets

cors.init_app(app)
socketio.init_app(app, cors_allowed_origins="*")

app.config['SECRET_KEY'] = secrets.token_hex(16)

@app.route('/')
def root():
    return 'I am root'

if __name__ == '__main__':
    print("link : http://127.0.0.1:5003")
    socketio.run(app, debug=False, port=5003)

