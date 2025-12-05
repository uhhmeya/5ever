import time
from flask.globals import request
from flask_socketio import emit # noqa
from .core.extensions import socketio # noqa
from .core.app import DB # noqa
from . import metrics as M # noqa

@socketio.on('set')
def Hset(data):
    k,v = data
    with M.track():
        time.sleep(0.001)
        DB.set(k,v)

@socketio.on('get')
def Hget(k):
    with M.track():
        time.sleep(0.001)
        DB.get(k)

@socketio.on('del')
def Hdel(k):
    with M.track():
        time.sleep(0.001)
        DB.delete(k)

@socketio.on('start')
def Hstart(exp):
    sid = request.sid
    M.start(exp, x=lambda y: socketio.emit('metrics', y, room=sid))







