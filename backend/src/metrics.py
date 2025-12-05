import threading
import time
from contextlib import contextmanager
from src.core.app import DB

S = threading.Lock()
_active = 0
_total = 0
_samples = []

L = threading.Lock()
_lats = []

exp_req = 0
start_time = None
dur = None
bthread = None
interval = 0.001
callback = None
_stop = False

def sample():
    while not _stop:
        with S:
            _samples.append(_active)
        time.sleep(interval)

@contextmanager
def track():
    global _active, _total, dur, bthread, callback, _stop
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
                _stop = True
                bthread.join(timeout=1) # noqa
                callback(get_metrics()) # noqa
                end()

def start(exp, x=None):
    global start_time, exp_req, bthread, callback, _stop
    start_time = time.time()
    exp_req = exp
    _stop = False
    bthread = threading.Thread(target=sample, daemon=True)
    bthread.start()
    callback = x

def end():
    global _active, _samples, _lats, _total, start_time, exp_req, dur, callback, bthread, _stop
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
    _stop = False


def get_metrics():
    slats = sorted(_lats)
    ssamp = sorted(_samples)
    ns = len(ssamp)
    nl = len(slats)
    return {'peak': max(_samples),'minC': ssamp[0],'meanC': sum(_samples) / ns,'p50C': ssamp[int(ns * 0.50)],'p95C': ssamp[int(ns * 0.95)],'p99C': ssamp[int(ns * 0.99)],'conten': sum(1 for s in _samples if s > 1) / ns * 100,'minL': min(_lats),'maxL': max(_lats),'meanL': sum(_lats) / nl,'p50L': slats[min(int(nl * 0.50), nl - 1)],'p95L': slats[min(int(nl * 0.95), nl - 1)],'p99L': slats[min(int(nl * 0.99), nl - 1)],'totalR': _total,'dur': dur}