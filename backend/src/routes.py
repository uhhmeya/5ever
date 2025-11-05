from flask_socketio import emit
from .core.extensions import socketio # noqa
from .core.app import db # noqa
from .helpers import extract # noqa
from .trackers.concurrency import Concurrency # noqa
from .trackers.time import Time # noqa
from .trackers.count import Counter # noqa


@socketio.on('set')
@extract('key', 'value')
def handle_set(key, value):
    with Concurrency.track():
        with Time.track():
            success = db.set(key, value)

    Counter.increment_total()
    Counter.increment_set()
    if success:
        Counter.increment_success()



@socketio.on('get')
@extract('key')
def handle_get(key):
    with Concurrency.track():
        with Time.track():
            db.get(key)

    Counter.increment_total()



@socketio.on('del')
@extract('key')
def handle_del(key):
    with Concurrency.track():
        with Time.track():
            db.delete(key)

    Counter.increment_total()


@socketio.on('get_metrics')
def handle_get_time_metrics():
    emit('metrics_response', {
        'time': Time.get_metrics(),
        'count': Counter.get_metrics(),
        'concurrency': Concurrency.get_metrics()
    })

@socketio.on('clear')
def handle_clear():
    db.data.clear()
    Time.clear()
    Counter.clear()
    Concurrency.clear()