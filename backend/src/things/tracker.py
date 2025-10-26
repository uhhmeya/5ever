import time
from ..helpers.metrics import (get_success_rate, get_min_latency, get_max_latency,get_mean_latency, get_p95_latency, get_p99_latency, get_p50_latency)

class MetricsTracker:
    def __init__(self):
        self.total_count = 0
        self.total_set_count = 0
        self.total_set_success_count = 0
        self.latencies = [] # time to update DB
        self.first = None # first req
        self.last = None # last req

    def add(self, operation_type, latency, success=None):

        if self.first is None:
            self.first = time.time()
        self.last = time.time()

        self.latencies.append(latency)
        self.total_count += 1

        if operation_type == 'set':
            self.total_set_count += 1
            if success:
                self.total_set_success_count += 1

    def get_metrics(self):
        duration = 0
        throughput = 0

        if self.first and self.last:
            duration = self.first - self.last
            if duration > 0:
                throughput = self.total_count / duration

        return {
            'total_set': self.total_set_count,
            'total_operations': self.total_count,
            'success_rate': get_success_rate(self.total_set_success_count, self.total_set_count),
            'min_latency': get_min_latency(self.latencies),
            'max_latency': get_max_latency(self.latencies),
            'mean_latency': get_mean_latency(self.latencies),
            'p50_latency': get_p50_latency(self.latencies),
            'p95_latency': get_p95_latency(self.latencies),
            'p99_latency': get_p99_latency(self.latencies),
            'duration': duration,
            'throughput': throughput
        }

    def reset(self):
        self.total_count = 0
        self.total_set_count = 0
        self.total_set_success_count = 0
        self.latencies = []
        self.first = None
        self.last = None

tracker = MetricsTracker()