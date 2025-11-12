from flask_socketio import emit
from .core.extensions import socketio # noqa
from .core.app import db # noqa
from .trackers.concurrency import Concurrency # noqa
from .trackers.latency import Latency # noqa
from .trackers.count import Counter # noqa

@socketio.on('set')
def handle_set(data):
    k,v = data
    with Concurrency.track():
        with Latency.track():
            db.set(k,v)
    Counter.increment()

@socketio.on('get')
def handle_get(k):
    with Concurrency.track():
        with Latency.track():
            db.get(k)
    Counter.increment()

@socketio.on('del')
def handle_del(k):
    with Concurrency.track():
        with Latency.track():
            db.delete(k)
    Counter.increment()

@socketio.on('get_metrics')
def handle_get_time_metrics():
    emit('metrics_response', {
        'time': Latency.get_metrics(),
        'count': Counter.get_metrics(),
        'concurrency': Concurrency.get_metrics()
    })

@socketio.on('clear')
def handle_clear():
    db.data.clear()
    Latency.clear()
    Counter.clear()
    Concurrency.clear()

@socketio.on('start_timer')
def start_timer(exp):
    Counter.start_timer(exp)