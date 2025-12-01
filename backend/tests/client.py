from gevent import monkey
monkey.patch_all()

from contextlib import contextmanager
import socketio
import random

def handle_response(*args):
    if not args:
        print("    get metrics was called too early \n")
        return
    print_results(args[0])

def make_client():
    sio = socketio.Client()
    sio.on('response', handle_response)
    sio.connect('http://localhost:5003')
    return sio

@contextmanager
def client():
    c = make_client()
    try : yield c
    finally : c.disconnect()

def send_req(c):
    x = random.randint(1, 3)
    if x == 1: c.emit('set', [f'key_{random.randint(0, 100)}', f'value_{random.randint(0, 1000)}'])
    elif x == 2: c.emit('get', f'key_{random.randint(0, 100)}')
    else: c.emit('del', f'key_{random.randint(0, 100)}')

def print_results(data):
    print(f"    Latency: min={data['minL']:.1f} max={data['maxL']:.1f} mean={data['meanL']:.1f} p50={data['p50L']:.1f} p95={data['p95L']:.1f} p99={data['p99L']:.1f} ms")
    print(f"    Count: r={data['totalR']} dur={data['dur']:.1f}s tput={data['totalR']/data['dur']:.1f}r/s")
    print(f"    Concurrency: peak={data['peak']} min={data['minC']} mean={data['meanC']:.1f} p50={data['p50C']} p95={data['p95C']} p99={data['p99C']} conten={data['conten']:.1f}% \n")