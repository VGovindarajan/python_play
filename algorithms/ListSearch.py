# https://runestone.academy/runestone/static/pythonds/AlgorithmAnalysis/ProgrammingExercises.html Problem 4 & 5
# Vijayarajan Govindarajan 2017

import functools
import random
import timeit


def GetListOfSizeN(size):
    return random.sample(range(10000000), size)


def GetLowestNumberInList(randomList):
    lowestNumber = 100000000000000000000000000000000
    for i in randomList:
        if i < lowestNumber:
            lowestNumber = i
            # print(lowestNumber)
    return lowestNumber


def runIt(size):
    print(size)
    randomList = GetListOfSizeN(size)
    # print(randomList)
    lowestNumber = GetLowestNumberInList(randomList)
    # print(lowestNumber)


A = 1


def main():
    for i in range(1000000, 10000000, 1000000):
        A = i
        t4 = timeit.Timer(functools.partial(runIt, A), "from __main__ import runIt")
        print("list range ", t4.timeit(number=10), "milliseconds")


if __name__ == "__main__":
    main()
