import threading

class Database:
    def __init__(self):
        self.data = {}
        self._lock = threading.Lock()

    def get(self, key):
        with self._lock:
            return self.data.get(key)

    def set(self, key, value):
        with self._lock:
            self.data[key] = value
            return True

    def delete(self, key):
        with self._lock:
            if key in self.data:
                del self.data[key]
                return True
            return False

    def clear(self):
        with self._lock:
            self.data.clear()
            return True