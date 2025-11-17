from tests.client import make_client
from tests.ratetest import rTest

if __name__ == '__main__':

    c = make_client()

    print("")
    for r in range(5000, 10_001, 2500):
        rTest(c,r,2)

    c.disconnect()











