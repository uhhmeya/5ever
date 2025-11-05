from tests.client import make_client
from tests.loadTest import run_load_test
import time

if __name__ == '__main__':

    client = make_client()
    client.connect('http://localhost:5003')

    for rate in range(2000, 3001, 500):

        client.emit('clear')
        time.sleep(0.67)

        run_load_test(client, rate, duration=2)
        time.sleep(0.67)

        client.emit('get_metrics')
        time.sleep(0.67)

    client.disconnect()











