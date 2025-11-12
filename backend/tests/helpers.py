import random
import time

def send_request(client):
    x = random.randint(1, 3)
    if x == 1 :
        client.emit('set', [k(), v()])
    elif x == 2 :
        client.emit('get', k())
    else:
        client.emit('del', k())

def wait_until(scheduled_time):
    now = time.time()
    if now < scheduled_time:
        time.sleep(scheduled_time - now)

def k():
    return f'key_{random.randint(0, 100)}'

def v():
    return f'value_{random.randint(0, 1000)}'
