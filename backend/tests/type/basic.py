def run_basic_tests(sio):

    # name = Alice
    sio.emit('set', {'key': 'name', 'value': 'Alice'})

    # get(name)
    sio.emit('get', {'key': 'name'})

    # get(age)
    sio.emit('get', {'key': 'age'})

    # age = 25
    sio.emit('set', {'key': 'age', 'value': 25})

    # get(age)
    sio.emit('get', {'key': 'age'})

    # del(name)
    sio.emit('del', {'key': 'name'})

    # get(name)
    sio.emit('get', {'key': 'name'})

    # del(naur)
    sio.emit('del', {'key': 'naur'})