import time
import threading
import socketio
import random
from contextlib import contextmanager

def rTest(r, dur, event):
    print(f"{r} r/s for {dur}s :")
    num_threads = 10
    threads = []
    total = int(r * dur)
    batch = total // num_threads
    rate = r / num_threads
    with client(event) as mc:
        mc.emit('start', total)
        for i in range(num_threads):
            w = threading.Thread(target=send, args=(batch, rate))
            w.start()
            threads.append(w)
        for t in threads: t.join()
        event.wait(timeout=30)
        event.clear()


def send(b, r):
    with client() as c:
        delay = 1.0 / r
        for _ in range(b):
            start = time.time()
            x = random.randint(1, 3)
            if x == 1: c.emit('set', [f'key_{random.randint(0, 100)}', f'value_{random.randint(0, 1000)}'])
            elif x == 2: c.emit('get', f'key_{random.randint(0, 100)}')
            else: c.emit('del', f'key_{random.randint(0, 100)}')
            elapsed = time.time() - start
            x = delay - elapsed
            if x > 0: time.sleep(x)

@contextmanager
def client(event=None):
    c = socketio.Client()
    if event: c.on('metrics', lambda data: (println(data), event.set()))
    c.connect('http://localhost:5003')
    try : yield c
    finally : c.disconnect()


def println(data):
    print(f"    Latency: min={data['minL']:.1f} max={data['maxL']:.1f} mean={data['meanL']:.1f} p50={data['p50L']:.1f} p95={data['p95L']:.1f} p99={data['p99L']:.1f} ms\n    Count: r={data['totalR']} dur={data['dur']:.1f}s tput={data['totalR']/data['dur']:.1f}r/s\n    Concurrency: peak={data['peak']} min={data['minC']} mean={data['meanC']:.1f} p50={data['p50C']} p95={data['p95C']} p99={data['p99C']} conten={data['conten']:.1f}%\n")

def main():
    print(" ")
    event = threading.Event()
    for r in range(10_000, 50_001, 20_000):
        rTest(r, 2, event)

if __name__ == '__main__':
    main()