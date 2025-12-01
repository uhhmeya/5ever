from tests.ratetest import rTest

def main() :
    print(" ")
    for r in range(10_000, 50_001, 10_000):
        rTest(r,2)


if __name__ == '__main__':
    main()















