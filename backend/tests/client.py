# tests/client.py
import socketio

def make_client():
    sio = socketio.Client()

    @sio.on('connect')
    def connect():
        print("Connected to server")

    @sio.on('disconnect')
    def disconnect():
        print("Disconnected from server")

    @sio.on('set_response')
    def handle_set_response(data):
        status = '✅' if data['success'] else '❌'
        print(f"[SET] {status} {data['key']} = {data['value']}")

    @sio.on('get_response')
    def handle_get_response(data):
        if data['value'] is None:
            print(f"[GET] ❌ {data['key']} = None")
        else:
            print(f"[GET] ✅ {data['key']} = {data['value']}")

    @sio.on('del_response')
    def handle_del_response(data):
        status = '✅' if data['success'] else '❌'
        print(f"[DEL] {status} {data['key']}")

    return sio