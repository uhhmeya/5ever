from flask_socketio import emit
from ...core.extensions import socketio
from ...core.app import db
from ...things.trackers.time import Time
from ...things.trackers.count import Counter
from ...helpers.extract import extract

@socketio.on('set')
@extract('key', 'value')
def handle_set(key, value):
    with Time.track():
        success = db.set(key, value)

    Counter.increment_total()
    Counter.increment_set()
    if success:
        Counter.increment_success()

    emit('set_response', {
        'success': success,
        'key': key,
        'value': value
    })

@socketio.on('get')
@extract('key')
def handle_get(key):
    with Time.track():
        result = db.get(key)

    Counter.increment_total()

    emit('get_response', {
        'key': key,
        'value': result,
    })


@socketio.on('del')
@extract('key')
def handle_del(key):
    with Time.track():
        found = db.delete(key)

    Counter.increment_total()

    emit('del_response', {
        'found': found,
        'key': key
    })

