import time
import threading
from contextlib import contextmanager


class TimeTracker:

    def __init__(self):
        self._lock = threading.Lock()
        self.latencies = []
        self.first = None

    @contextmanager
    def track(self):
        start = time.time()
        try : yield
        finally:
            end = time.time()
            latency = (end - start) * 1000
            with self._lock:
                if self.first is None:
                    self.first = start # start timer
                self.latencies.append(latency) # log latency

    def clear(self):
        with self._lock:
            self.latencies = []
            self.first = None

    # must be called at end
    def get_metrics(self):
        duration = time.time() - self.first
        return {
            'min_latency': self._get_min_latency(self.latencies),
            'max_latency': self._get_max_latency(self.latencies),
            'mean_latency': self._get_mean_latency(self.latencies),
            'p50_latency': self._get_p50_latency(self.latencies),
            'p95_latency': self._get_p95_latency(self.latencies),
            'p99_latency': self._get_p99_latency(self.latencies),
            'duration': duration,
        }

    @staticmethod
    def _get_success_rate(success_count, total_count):
        if total_count == 0:
            return 0.0
        return (success_count / total_count) * 100

    @staticmethod
    def _get_min_latency(latencies):
        if not latencies:
            return 0.0
        return min(latencies)

    @staticmethod
    def _get_max_latency(latencies):
        if not latencies:
            return 0.0
        return max(latencies)

    @staticmethod
    def _get_mean_latency(latencies):
        if not latencies:
            return 0.0
        return sum(latencies) / len(latencies)

    @staticmethod
    def _get_p95_latency(latencies):
        if not latencies:
            return 0.0
        sorted_lats = sorted(latencies)
        p95_index = int(len(sorted_lats) * 0.95)
        return sorted_lats[p95_index]

    @staticmethod
    def _get_p99_latency(latencies):
        if not latencies:
            return 0.0
        sorted_lats = sorted(latencies)
        p99_index = int(len(sorted_lats) * 0.99)
        return sorted_lats[p99_index]

    @staticmethod
    def _get_p50_latency(latencies):
        if not latencies:
            return 0.0
        sorted_lats = sorted(latencies)
        p50_index = int(len(sorted_lats) * 0.50)
        return sorted_lats[p50_index]

Time = TimeTracker()