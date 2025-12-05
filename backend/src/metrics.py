import gevent
import time
from datetime import datetime
from gevent.lock import Semaphore
from contextlib import contextmanager
from src.core.app import DB

S = Semaphore()
_active = 0
_total = 0
_samples = []

L = Semaphore()
_lats = []

# 1 wr only
exp_req = 0
start_time = None
dur = None
bthread = None
interval = 0.00000000000000000000000000001
callback = None


def sample():
    while True:
        with S:
            _samples.append(_active)
        gevent.sleep(interval)

@contextmanager
def track():
    global _active, _total, dur, bthread, callback
    with S:
        _active += 1
    s = time.time()
    try: yield
    finally:
        l = (time.time()-s)*1000
        with L:
            _lats.append(l)
        with S:
            _active -= 1
            _total += 1
            if _total == exp_req:
                dur = time.time() - start_time
                gevent.kill(bthread)
                bthread = None
                callback(get_metrics())  # noqa
                end()

def start(exp, x=None):
    global start_time, exp_req, bthread, callback
    start_time = time.time()
    exp_req = exp
    bthread = gevent.spawn(sample)
    callback = x

def end():
    global _active, _samples, _lats, _total, start_time, exp_req, dur, callback, bthread
    DB.data.clear()
    _active = 0
    exp_req = 0
    _total = 0
    _samples = []
    _lats = []
    start_time = None
    dur = None
    bthread = None
    callback = None


def get_metrics():
    slats = sorted(_lats)
    ssamp = sorted(_samples)
    ns = len(ssamp)
    nl = len(slats)
    return {'peak': max(_samples),'minC': ssamp[0],'meanC': sum(_samples) / ns,'p50C': ssamp[int(ns * 0.50)],'p95C': ssamp[int(ns * 0.95)],'p99C': ssamp[int(ns * 0.99)],'conten': sum(1 for s in _samples if s > 1) / ns * 100,'minL': min(_lats),'maxL': max(_lats),'meanL': sum(_lats) / nl,'p50L': slats[min(int(nl * 0.50), nl - 1)],'p95L': slats[min(int(nl * 0.95), nl - 1)],'p99L': slats[min(int(nl * 0.99), nl - 1)],'totalR': _total,'dur': dur}