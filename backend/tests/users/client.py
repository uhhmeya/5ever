import socketio

def make_client():
    sio = socketio.Client()

    @sio.on('set_response')
    def handle_set_response(data):
        key = data['key']
        value = data['value']
        latency = data.get('latency', 0)

        if data['success']:
            status = '✅'
        else:
            status = '❌'

        print(f"[SET] {status} {key} = {value} ({latency:.2f}ms)")

    @sio.on('get_response')
    def handle_get_response(data):
        key = data['key']
        value = data['value']
        print(f"[GET] {key} = {value}")

    @sio.on('del_response')
    def handle_del_response(data):
        key = data['key']

        if data['change']:
            print(f"[DEL] {key} (found)")
        else:
            print(f"[DEL] {key} (not found)")

    return sio