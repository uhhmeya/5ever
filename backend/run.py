import logging
from src.core.app import create_app
from src.core.extensions import socketio

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = create_app()

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5003, debug=False, use_reloader=False, log_output=False)