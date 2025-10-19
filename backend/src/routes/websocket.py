from .. import socketio # get socketio from app.py

@socketio.on('connect')
def handle_connect():
    print('connect handler called')

@socketio.on('disconnect')
def handle_disconnect():
    print('disconnect handler called')

@socketio.on('user_id')
def handle_user_id(data):
    user_id = data.get('userId')
    print(f'userID handler called for {user_id}')


