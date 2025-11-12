import time
from .helpers import wait_until, send_request

def run_rate_test(client, rate, duration):
    print(f"\n{'='*60}")
    print(f"Running {rate} req/sec for {duration}s")
    print(f"{'='*60}")

    exp = int(rate * duration)
    interval = 1.0/rate
    client.emit('clear')
    client.emit('start_timer', exp)
    start = time.time()

    for i in range(exp):
        x = start + i * interval
        wait_until(x)
        send_request(client)

    time.sleep(1)
    client.emit('get_metrics')
    time.sleep(1)