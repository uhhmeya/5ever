import time
import random

KEY_POOL_SIZE = 100
VALUE_POOL_SIZE = 1000
OPERATIONS = ['get', 'set', 'del']

def run_load_test(client, load, duration):

    print(f"\n{'='*100}")
    print(f"Running {load} req/sec for {duration}s")
    print(f"{'='*100}")

    time_between_requests = 1.0 / load
    end_time = time.time() + duration

    while time.time() < end_time:
        start = time.time()
        operation = random.choice(['get', 'set', 'del'])

        key = f'key_{random.randint(0, KEY_POOL_SIZE)}' # key_x


        if operation == 'set':
            value = f'value_{random.randint(0, VALUE_POOL_SIZE)}'
            client.emit('set', {'key': key, 'value': value})

        elif operation == 'get':
            client.emit('get', {'key': key})

        else:
            client.emit('del', {'key': key})

        # maintain rate
        elapsed = time.time() - start
        sleep_time = max(0, time_between_requests - elapsed)
        time.sleep(sleep_time)
