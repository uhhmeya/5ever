import time
from tests.users.client import make_client
from tests.users.admin import make_admin
from tests.type.basic import run_basic_tests

if __name__ == '__main__':
    admin = make_admin()
    admin.connect('http://localhost:5003')
    admin.emit('clear')

    bro1 = make_client()
    bro1.connect('http://localhost:5003')

    print("\n=== TESTING ===")
    run_basic_tests(bro1)
    time.sleep(0.1)

    admin.emit('get_metrics')
    time.sleep(0.1)

    bro1.disconnect()
    admin.disconnect()

