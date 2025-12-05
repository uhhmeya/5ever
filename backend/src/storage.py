from gevent.lock import Semaphore

class Database:

    def __init__(self):
        self.data = {}
        self.lock = Semaphore() 

    def get(self, k):
        return self.data.get(k)

    def set(self, k, v):
        with self.lock:
            self.data[k] = v
            return True

    def delete(self, k):
        if k in self.data:
            del self.data[k]
            return True
        return False

    def clear(self):
        with self.lock:
            self.data.clear()
            return True