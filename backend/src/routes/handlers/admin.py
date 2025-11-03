from flask_socketio import emit
from ...core.extensions import socketio
from ...core.app import db
from ...things.trackers.time import Time
from ...things.trackers.count import Counter

@socketio.on('clear')
def handle_clear():
    db.data.clear()
    Time.clear()
    Counter.clear()

@socketio.on('get_metrics')
def handle_get_time_metrics():
    time_metrics = Time.get_metrics()
    count_metrics = Counter.get_metrics()
    emit('metrics_response', {
        'time': time_metrics,
        'count': count_metrics
    })