from gevent import monkey
monkey.patch_all()

import logging
from src.core.app import create_app # creates DB
from src.core.extensions import socketio
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

app = create_app()

if __name__ == '__main__':
    http_server = WSGIServer(('127.0.0.1', 5003),app, handler_class=WebSocketHandler,log=None,error_log=None)
    http_server.serve_forever()

