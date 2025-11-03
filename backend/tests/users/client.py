import socketio
from ..helpers.extract import extract


def make_client():
    sio = socketio.Client()

    @sio.on('set_response')
    @extract('key', 'value', 'success')
    def handle_set_response(key, value, success):
        status = '✅' if success else '❌'
        print(f"[SET] {status} {key} = {value}")

    @sio.on('get_response')
    @extract('key', 'value')
    def handle_get_response(key, value):
        print(f"[GET] {key} = {value}")

    @sio.on('del_response')
    @extract('key', 'found')
    def handle_del_response(key, found):
        if found: print(f"[DEL] {key} (found)")
        else: print(f"[DEL] {key} (not found)")

    return sio