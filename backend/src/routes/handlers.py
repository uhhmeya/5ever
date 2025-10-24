from flask_socketio import emit
from ..extensions import socketio
from ..app import db

print("registered socket handlers")

@socketio.on('connect')
def handle_connect():
    print("connect handler called")

@socketio.on('disconnect')
def handle_disconnect():
    print('disconnect handler called')

@socketio.on('set')
def handle_set(data):
    key = data.get('key')
    value = data.get('value')
    success = db.set(key, value)
    emit('set_response', {
        'success': success,
        'key': key,
        'value': value
    })

@socketio.on('get')
def handle_get(data):
    key = data.get('key')
    result = db.get(key)
    emit('get_response', {
        'key': key,
        'value': result,
    })

@socketio.on('del')
def handle_del(data):
    key = data.get('key')
    success = db.delete(key)
    emit('del_response', {
        'success': success,
        'key': key
    })


