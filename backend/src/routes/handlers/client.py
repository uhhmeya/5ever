import time
from flask_socketio import emit
from ...core.extensions import socketio
from ...core.app import db
from ...things.tracker import tracker


@socketio.on('set')
def handle_set(data):
    start = time.time()

    key = data.get('key')
    value = data.get('value')
    success = db.set(key, value)

    latency = (time.time() - start) * 1_000
    tracker.add('set', latency, success=success)

    emit('set_response', {
        'success': success,
        'key': key,
        'value': value,
        'latency': latency
    })


@socketio.on('get')
def handle_get(data):
    start = time.time()

    key = data.get('key')
    result = db.get(key)

    latency = (time.time() - start) * 1_000
    tracker.add('get', latency)

    emit('get_response', {
        'key': key,
        'value': result,
    })

@socketio.on('del')
def handle_del(data):
    start = time.time()

    key = data.get('key')
    change = db.delete(key)

    latency = (time.time() - start) * 1_000
    tracker.add('del', latency)

    emit('del_response', {
        'change': change,
        'key': key
    })