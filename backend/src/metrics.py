import threading
from contextlib import contextmanager
import time

S = threading.Lock()
_active = 0
_peak = 0
_samples = []
_total = 0

L = threading.Lock()
_lats = []

# only written once
EXP = 0
START = None
DUR = None

@contextmanager
def track():
    global _active, _peak, _total, DUR

    with S:
        _active += 1
        _peak = max(_peak, _active)
        _samples.append(_active)

    s = time.time()
    try: yield
    finally:
        l = (time.time()-s)*1000

        with L:
            _lats.append(l)

        with S:
            _active -= 1
            _samples.append(_active)
            _total += 1

            if _total == EXP :
                DUR = time.time() - START

def start(exp):
    global START, EXP
    START = time.time()
    EXP = exp

def clear():
    global _active, _peak, _samples, _lats, _total, START, EXP, DUR
    _active = 0
    _peak = 0
    _samples = []
    _lats = []
    _total = 0
    START = None
    EXP = 0
    DUR = None


def get_metrics():
    slats = sorted(_lats)
    ssamp = sorted(_samples)
    ns = len(ssamp)
    nl = len(slats)
    meanc = sum(_samples) / ns

    return {
        'peak': _peak,
        'minC': ssamp[0],
        'meanC': meanc,
        'p50C': ssamp[int(ns * 0.50)],
        'p95C': ssamp[int(ns * 0.95)],
        'p99C': ssamp[int(ns * 0.99)],
        'conten': sum(1 for s in _samples if s > 1) / ns * 100,
        'minL': min(_lats),
        'maxL': max(_lats),
        'meanL': sum(_lats) / nl,
        'p50L': slats[min(int(nl * 0.50), nl - 1)],
        'p95L': slats[min(int(nl * 0.95), nl - 1)],
        'p99L': slats[min(int(nl * 0.99), nl - 1)],
        'totalR': _total,
        'dur': DUR
    }