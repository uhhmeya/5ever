from flask_socketio import emit
from ...core.extensions import socketio
from ...core.app import db
from ...things.tracker import tracker

@socketio.on('clear_db')
def handle_reset_db():
    db.data.clear()
    emit('reset_response', {'success': True})

@socketio.on('get_metrics')
def handle_get_metrics():
    metrics = tracker.get_metrics()
    emit('metrics_response', metrics)

@socketio.on('clear_metrics')
def handle_clear_metrics():
    tracker.reset()
    emit('clear_metrics_response', {'success': True})