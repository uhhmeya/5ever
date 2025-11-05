import threading
from contextlib import contextmanager


class ConcurrencyTracker:

    def __init__(self):
        self._lock = threading.Lock()
        self._active = 0
        self._peak = 0
        self._samples = []

    @contextmanager
    def track(self):
        with self._lock:
            self._active += 1
            if self._active > self._peak:
                self._peak = self._active
            self._samples.append(self._active)
        try: yield
        finally:
            with self._lock:
                self._active -= 1

    def get_metrics(self):
        with self._lock:
            return {
                'peak_concurrent': self._peak,
                'min_concurrent': min(self._samples) if self._samples else 0,
                'mean_concurrent': self._get_mean(self._samples),
                'std_dev_concurrent': self._get_std_dev(self._samples),
                'p50_concurrent': self._get_percentile(self._samples, 0.50),
                'p95_concurrent': self._get_percentile(self._samples, 0.95),
                'p99_concurrent': self._get_percentile(self._samples, 0.99),
                'contention_rate': (sum(1 for s in self._samples if s > 1) / len(self._samples) * 100) if self._samples else 0.0,
            }

    def clear(self):
        with self._lock:
            self._active = 0
            self._peak = 0
            self._samples = []

    @staticmethod
    def _get_mean(samples):
        if not samples:
            return 0.0
        return sum(samples) / len(samples)

    @staticmethod
    def _get_std_dev(samples):
        if not samples:
            return 0.0
        mean = sum(samples) / len(samples)
        variance = sum((x - mean) ** 2 for x in samples) / len(samples)
        return variance ** 0.5

    @staticmethod
    def _get_percentile(samples, percentile):
        if not samples:
            return 0.0
        sorted_samples = sorted(samples)
        index = int(len(sorted_samples) * percentile)
        return sorted_samples[index]

Concurrency = ConcurrencyTracker()