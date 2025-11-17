from flask_socketio import emit
from .core.extensions import socketio # noqa
from .core.app import db # noqa
from . import metrics as m # noqa


@socketio.on('set')
def hset(data):
    k,v = data
    with m.track():
        db.set(k,v)

@socketio.on('get')
def hget(k):
    with m.track():
        db.get(k)

@socketio.on('del')
def hdel(k):
    with m.track():
        db.delete(k)

@socketio.on('metrics')
def hgm():
    emit('response', m.get_metrics())

@socketio.on('clear')
def hclear():
    db.data.clear()
    m.clear()

@socketio.on('start')
def hstart(exp):
    m.start(exp)

