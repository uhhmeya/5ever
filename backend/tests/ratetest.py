import random
import time

def rTest(c,r,dur):

    print(f"{r} r/s for {dur}s :")

    exp = int(r * dur)
    t = 1.0/r

    c.emit('clear')
    c.emit('start', exp)

    s = time.time()

    for i in range(exp):
        x = s+i*t
        wait_until(x)
        send_request(c)

    c.emit('metrics')

    time.sleep(0.2)


def send_request(c):
    x = random.randint(1, 3)
    if x == 1 : c.emit('set', [k(), v()])
    elif x == 2 : c.emit('get', k())
    else: c.emit('del', k())

def wait_until(x):
    now = time.time()
    if now < x:
        time.sleep(x-now)

def k(): return f'key_{random.randint(0, 100)}'

def v(): return f'value_{random.randint(0, 1000)}'