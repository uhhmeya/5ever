import time

def run_basic_tests(sio):

    # name = Alice
    sio.call('set', {'key': 'name', 'value': 'Alice'})

    # get(name)
    sio.call('get', {'key': 'name'})

    # get(age)
    sio.call('get', {'key': 'age'})

    # age = 25
    sio.call('set', {'key': 'age', 'value': 25})

    # get(age)
    sio.call('get', {'key': 'age'})

    # del(name)
    sio.call('del', {'key': 'name'})

    # get(name)
    sio.call('get', {'key': 'name'})

    # del(naur)
    sio.call('del', {'key': 'naur'})