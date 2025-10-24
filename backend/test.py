import time
from tests.client import make_client
from tests.cases import run_tests

if __name__ == '__main__':
    sio = make_client()
    sio.connect('http://localhost:5003')

    run_tests(sio)
    time.sleep(1)

    sio.disconnect()