from src.core.app import create_app # creates DB
from src.core.extensions import socketio

app = create_app()

if __name__ == '__main__':
    print(f"Link http://127.0.0.1:5003")
    socketio.run(app, debug=False, host='127.0.0.1', port=5003)