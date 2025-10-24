from flask_socketio import emit
from ..extensions import socketio
from ..app import db

print("=" * 50)
print("SOCKET HANDLERS LOADING...")
print("=" * 50)

@socketio.on('connect')
def handle_connect():
    print('=' * 50)
    print('CONNECT HANDLER CALLED')
    print('=' * 50)
    emit('connection_response', {'status': 'connected'})

@socketio.on('disconnect')
def handle_disconnect():
    print('DISCONNECT HANDLER CALLED')

@socketio.on('set')
def handle_set(data):
    key = data.get('key')
    value = data.get('value')
    db.set(key, value)
    print(f'SET: {key} = {value}')
    emit('set_response', {'success': True, 'key': key})

@socketio.on('get')
def handle_get(data):
    key = data.get('key')
    result = db.get(key)
    print(f'GET: {key} -> {result}')
    emit('get_response', {'key': key, 'value': result})

@socketio.on('del')
def handle_del(data):
    key = data.get('key')
    db.delete(key)
    print(f'DEL: {key}')
    emit('del_response', {'success': True, 'key': key})