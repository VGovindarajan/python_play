# https://runestone.academy/runestone/static/pythonds/Recursion/pythondsProgrammingExercises.html
# Vijayarajan Govindarajan 2017

import functools
import timeit

# 1.Write a recursive function to compute the factorial of a number.
def factorialRecursion(n):
    # base case
    if n <= 1:
        return 1;
    else:
        return n * factorialRecursion(n - 1)


# 2.Write a recursive function to reverse a list.

def reverseListRecursion(listToReverse):
    # print(listToReverse)
    listLen = len(listToReverse)
    # baseCase
    if listLen <= 1:
        return listToReverse
    else:
        reversed = reverseListRecursion(listToReverse[0:listLen - 1])
        current = listToReverse[listLen - 1]
        reversed.insert(0, current)
        return reversed


# 5. Write a recursive function to compute the Fibonacci sequence. How does the performance of the recursive function compare to that of an iterative version?
# https://en.wikipedia.org/wiki/Fibonacci_number#List_of_Fibonacci_numbers
def FibonacciR(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciR(n - 1) + FibonacciR(n - 2)


def FibSeriesR(n):
    retVal = []
    for i in range(n + 1):
        retVal.append(FibonacciR(i))
    return retVal


def FibonacciI(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev = 1
        current = 1
        for i in range(2, n):
            total = prev + current
            prev = current
            current = total
    return current


def FibSeriesI(n):
    retVal = []
    for i in range(n + 1):
        retVal.append(FibonacciI(i))
    return retVal


def FibonacciM(n, fibDictionary):
    if n <= 0:
        return fibDictionary[0]
    elif n == 1:
        return fibDictionary[1]
    else:
        for i in range(2, n+1):
            total = fibDictionary[i-1] + fibDictionary[i-2]
            fibDictionary[i] = total
    return fibDictionary[n]


def FibSeriesM(n):
    retVal = []
    fibDictionary = {1: 1, 0: 0}
    for i in range(n + 1):
        retVal.append(FibonacciM(i, fibDictionary))
    return retVal

def test_time_taken():
    for i in range(10, 100, 10):

        testFibSeriesR = timeit.Timer(functools.partial(FibSeriesR, i), "from __main__ import FibSeriesR")
        fibSeriesRTime =  testFibSeriesR.timeit(number=10)

        testFibSeriesI = timeit.Timer(functools.partial(FibSeriesI, i), "from __main__ import FibSeriesI")
        fibSeriesITime =  testFibSeriesI.timeit(number=10)

        testFibSeriesM = timeit.Timer(functools.partial(FibSeriesM, i), "from __main__ import FibSeriesM")
        fibSeriesMTime = testFibSeriesM.timeit(number=10)
        print("%d, FibSeriesR = %f, FibSeriesI = %f, FibSeriesM = %f" %(i, fibSeriesRTime, fibSeriesITime, fibSeriesMTime))


def main():
    # print(factorialRecursion(5))

    # print(factorialRecursion(969))
    # print(reverseListRecursion([1,2,3,4,5,7,8,9,10,11,12,13,14,15]))

    #print(FibonacciR(20))
    print(FibSeriesR(20))

    #print(FibonacciI(20))
    print(FibSeriesI(20))

    fibDictionary = {1: 1, 0: 0}
    #print(FibonacciM(20))
    print(FibSeriesM(20))
    test_time_taken()

if __name__ == "__main__":
    main()
