from flask_socketio import emit
from .core.extensions import socketio
from .core.app import db
from . import metrics as m

@socketio.on('set')
def Hset(data):
    k,v = data
    with m.track():
        db.set(k,v)

@socketio.on('get')
def Hget(k):
    with m.track():
        db.get(k)

@socketio.on('del')
def Hdel(k):
    with m.track():
        db.delete(k)

@socketio.on('metrics')
def Hmet():
    emit('response', m.get_metrics())

@socketio.on('start')
def Hstart(exp):
    m.clear()
    db.data.clear()
    m.start(exp)






