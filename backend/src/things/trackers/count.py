import threading



class RequestCounter:

    def __init__(self):
        self._lock = threading.Lock()
        self._total = 0
        self._set_total = 0
        self._success = 0


    def increment_total(self):
        with self._lock:
            self._total += 1

    def increment_set(self):
        with self._lock:
            self._set_total += 1

    def increment_success(self):
        with self._lock:
            self._success += 1

    def get_metrics(self):
        with self._lock:
            return {
                'total_requests': self._total,
                'set_success': self._success,
                'set_failure': self._set_total - self._success,
            }

    def clear(self):
        with self._lock:
            self._total = 0
            self._set_total = 0
            self._success = 0

Counter = RequestCounter()