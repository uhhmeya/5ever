import time

def run_tests(sio):
    print("\n=== Testing Database Operations ===\n")

    print("1. Testing SET...")
    sio.emit('set', {'key': 'name', 'value': 'Alice'})
    time.sleep(0.5)

    print("2. Testing GET (existing key)...")
    sio.emit('get', {'key': 'name'})
    time.sleep(0.5)

    print("3. Testing GET (non-existent key)...")
    sio.emit('get', {'key': 'age'})
    time.sleep(0.5)

    print("4. Testing SET (another key)...")
    sio.emit('set', {'key': 'age', 'value': 25})
    time.sleep(0.5)

    print("5. Testing GET (new key)...")
    sio.emit('get', {'key': 'age'})
    time.sleep(0.5)

    print("6. Testing DEL...")
    sio.emit('del', {'key': 'name'})
    time.sleep(0.5)

    print("7. Testing GET (after delete)...")
    sio.emit('get', {'key': 'name'})
    time.sleep(0.5)

    print("8. Testing DEL (non-existent key)...")
    sio.emit('del', {'key': 'nonexistent'})
    time.sleep(0.5)

    print("\n=== Tests Complete ===\n")