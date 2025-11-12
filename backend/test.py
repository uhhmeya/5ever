from tests.client import make_client
from tests.rateTest import run_rate_test

if __name__ == '__main__':

    client = make_client()
    client.connect('http://localhost:5003')

    for rate in range(2000, 3001, 500):
        run_rate_test(client, rate, duration=2)


    client.disconnect()











