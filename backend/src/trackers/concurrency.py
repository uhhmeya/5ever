import threading
from contextlib import contextmanager


class ConcurrencyTracker:

    def __init__(self):
        self.lock = threading.Lock()
        self.active = 0
        self.peak = 0
        self.samples = []

    @contextmanager
    def track(self):
        with self.lock:
            self.active += 1
            if self.active > self.peak:
                self.peak = self.active
            self.samples.append(self.active)
        try: yield
        finally:
            with self.lock:
                self.active -= 1

    def get_metrics(self):
        with self.lock:
            copy = self.samples.copy()
            peak = self.peak

        sorteds = sorted(copy)
        n = len(sorteds)
        μ = sum(copy) / n

        return {
            'peak_concurrent': peak,
            'min_concurrent': sorteds[0],
            'mean_concurrent': μ,
            'std_dev_concurrent': (sum((x - μ) ** 2 for x in copy) / n) ** 0.5,
            'p50_concurrent': sorteds[int(n * 0.50)],
            'p95_concurrent': sorteds[int(n * 0.95)],
            'p99_concurrent': sorteds[int(n * 0.99)],
            'contention_rate': (sum(1 for s in copy if s > 1) / n * 100),
        }

    def clear(self):
        with self.lock:
            self.active = 0
            self.peak = 0
            self.samples = []


Concurrency = ConcurrencyTracker()