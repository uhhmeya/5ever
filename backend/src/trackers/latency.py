import time
import threading
from contextlib import contextmanager


class LatencyTracker:
    def __init__(self):
        self.lock = threading.Lock()
        self.latencies = []

    @contextmanager
    def track(self):
        start = time.time()
        try:
            yield
        finally:
            end = time.time()
            latency = (end - start) * 1000
            with self.lock:
                self.latencies.append(latency)

    def clear(self):
        with self.lock:
            self.latencies = []

    def get_metrics(self):
        return {
            'min_latency': self._get_min_latency(self.latencies),
            'max_latency': self._get_max_latency(self.latencies),
            'mean_latency': self._get_mean_latency(self.latencies),
            'p50_latency': self._get_p50_latency(self.latencies),
            'p95_latency': self._get_p95_latency(self.latencies),
            'p99_latency': self._get_p99_latency(self.latencies),
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
        # Fixed: Ensure index is within bounds
        p95_index = min(int(len(sorted_lats) * 0.95), len(sorted_lats) - 1)
        return sorted_lats[p95_index]

    @staticmethod
    def _get_p99_latency(latencies):
        if not latencies:
            return 0.0
        sorted_lats = sorted(latencies)
        p99_index = min(int(len(sorted_lats) * 0.99), len(sorted_lats) - 1)
        return sorted_lats[p99_index]

    @staticmethod
    def _get_p50_latency(latencies):
        if not latencies:
            return 0.0
        sorted_lats = sorted(latencies)
        p50_index = min(int(len(sorted_lats) * 0.50), len(sorted_lats) - 1)
        return sorted_lats[p50_index]

Latency = LatencyTracker()