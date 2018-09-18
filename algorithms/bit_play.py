# Vijayarajan Govindarajan 2018

import functools
import timeit

def isOddCheckBitImpl(number):
    return (1 & number) == 1

def isOddCheckModuloImpl(number):
    return (number%2) == 1

def two_raised_to_the_power(number):
    return (1 << number)

def test_time_taken():
    for i in range(1000, 2000, 1):
        bitCheck = timeit.Timer(functools.partial(isOddCheckBitImpl, i), "from __main__ import isOddCheckBitImpl")
        bitCheckTime = bitCheck.timeit(number=10000)

        modCheck = timeit.Timer(functools.partial(isOddCheckModuloImpl, i), "from __main__ import isOddCheckModuloImpl")
        modCheckTime = modCheck.timeit(number=10000)

        #print("%d, bitCheckTime = %f, modCheckTime = %f, % "(i, bitCheckTime, modCheckTime))
        print(i, bitCheckTime, modCheckTime)

def main():
    for i in range(0,500):
        #print(i, isOddCheckBitImpl(i), isOddCheckModuloImpl(i))
        #assert ( isOddCheckBitImpl(i)== isOddCheckModuloImpl(i))
        print(i, two_raised_to_the_power(i))
    print("")

if __name__ == "__main__":
    main()