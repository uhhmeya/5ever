import socketio
import time

sio = socketio.Client()

@sio.on('connect')
def connect():
    print("Client connected to server")
    sio.emit('get', {'key': 'test'})

@sio.on('disconnect')
def disconnect():
    print("Client disconnected from server")

@sio.on('response')
def response(data):
    print(data)

if __name__ == '__main__':
    sio.connect('http://localhost:5003')
    time.sleep(2)
    sio.disconnect()