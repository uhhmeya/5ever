import threading
import time

class CountTracker:

    def __init__(self):
        self.lock = threading.Lock()
        self.total = 0
        self.exp = 0
        self.start = None
        self.duration = None

    def start_timer(self, exp):
        with self.lock:
            self.start = time.time()
            self.exp = exp

    def increment(self):
        with self.lock:
            self.total += 1
            if self.total >= self.exp:
                self.duration = time.time() - self.start


    def get_metrics(self):
        with self.lock:
            return {
                'total_requests': self.total,
                'duration' : self.duration
            }

    def clear(self):
        with self.lock:
            self.total = 0
            self.start = None
            self.exp = 0
            self.duration = None

Counter = CountTracker()