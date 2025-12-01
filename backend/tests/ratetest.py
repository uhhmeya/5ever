from gevent import monkey
monkey.patch_all()

import time
import threading
from tests.client import make_client, send_req, client

def rTest(r, dur):
    print(f"{r} r/s for {dur}s :")

    num_threads = 10
    threads = []
    total = int(r * dur)
    batch = total // num_threads
    rate = r / num_threads

    with client() as mc:
        mc.emit('start', total)
        for i in range(num_threads):
            w = threading.Thread(target=send_batch, args=(batch, rate))
            w.start()
            threads.append(w)
        for thread in threads: thread.join() # blocks mc
        mc.emit('metrics')
        time.sleep(10)  # fix

def wait(delay, start):
    elapsed = time.time() - start
    x = delay - elapsed
    if x > 0:
        time.sleep(x)

def send_batch(b, r):
    with client() as c:
        delay = 1.0 / r
        for _ in range(b):
            start = time.time()
            send_req(c)
            wait(delay, start)