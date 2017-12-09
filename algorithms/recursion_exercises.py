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
        for i in range(2, n + 1):
            total = fibDictionary[i - 1] + fibDictionary[i - 2]
            fibDictionary[i] = total
    return fibDictionary[n]


def FibSeriesM(n):
    retVal = []
    fibDictionary = {1: 1, 0: 0}
    for i in range(n + 1):
        retVal.append(FibonacciM(i, fibDictionary))
    return retVal


# 15.This problem is called the string edit distance problem, and is quite useful in many areas of research.
#  Suppose that you want to transform the word “algorithm” into the word “alligator.”
#  For each letter you can either copy the letter from one word to another at a cost of 5,
# you can delete a letter at cost of 20, or insert a letter at a cost of 20. The total cost to transform one word
#  into another is used by spell check programs to provide suggestions for words that are close to one another.
# Use dynamic programming techniques to develop an algorithm that gives you the smallest edit distance between
#  any two words.

def getCopyCost(fromWord, toWord, copyCost, deleteCost, insertCost):
    # both words are same
    if fromWord == toWord:
        return 0

    # to word is empty or equal length
    if len(toWord) == 0:
        print("COPY WORD: From ", fromWord, " to ", toWord)
        return len(fromWord) * copyCost

    if len(toWord) == len(fromWord):
        cost = 0
        fromList = [i for i in fromWord]
        toList = [j for j in toWord]
        lenOfWord = len(fromWord)
        for k in range(lenOfWord):
            if fromList[k] is not toList[k]:
                print("COPY LETTER: Change From ", fromList[k], " to ", toList[k])
                fromList[k] = toList[k]
                cost += copyCost
        return cost

    return None


def getDeleteCost(fromWord, toWord, copyCost, deleteCost, insertCost):
    # both words are same
    if fromWord == toWord:
        return 0

    # to word is empty
    if len(toWord) == 0:
        return len(fromWord) * deleteCost

    if len(toWord) < len(fromWord):
        cost = 0
        fromList = [i for i in fromWord]
        lenOfToWord = len(toWord)
        lenOfFromWord = len(fromWord)
        for l in range(lenOfToWord, lenOfFromWord):
             print("DELETE LETTER: ", fromList[l])
             cost += deleteCost
        return cost

    return None

def getInsertCost(fromWord, toWord, copyCost, deleteCost, insertCost):
    # both words are same
    if fromWord == toWord:
        return 0

    # from word is empty
    if len(fromWord) == 0:
        return len(toWord) * insertCost

    if len(toWord) > len(fromWord):
        cost = 0
        toList = [j for j in toWord]
        lenOfToWord = len(toWord)
        lenOfFromWord = len(fromWord)
        for l in range(lenOfFromWord, lenOfToWord):
             print("INSERT LETTER: ", toList[l])
             cost += insertCost
        return cost

    return None


def getMinCost(fromWord, toWord, copyCost, deleteCost, insertCost):
    print(fromWord, toWord)
    fromList = [i for i in fromWord]
    toList = [j for j in toWord]
    totalCost = 0
    operationSteps = []
    maxlen = max(len(fromWord), len(toWord))
    for i in range(maxlen):
        fromSlice = fromList[i:i+1]
        toSlice = toList[i:i+1]
        operationCost = 10000
        operationStep = "leave alone " + str(fromSlice)
        print(fromSlice, toSlice)
        copy = getCopyCost(fromSlice, toSlice, copyCost, deleteCost, insertCost)
        if copy is not None:
            print("copy cost", copy)
            if copy < operationCost and copy > 0:
                operationCost = copy
                operationStep = "Copy " + str(toSlice)
        delete = getDeleteCost(fromSlice, toSlice, copyCost, deleteCost, insertCost)
        if delete is not None and not 0:
            print("delete cost", delete)
            if delete < operationCost  and delete > 0:
                operationCost = delete
                operationStep = "Delete " + str(fromSlice)

        insert = getInsertCost(fromSlice, toSlice, copyCost, deleteCost, insertCost)
        if insert is not None and not 0:
            print("insert cost", insert)
            if insert < operationCost  and insert > 0:
                operationCost = insert
                operationStep = "insert " + str(toSlice)

        if operationCost is not 10000:
            totalCost += operationCost
        operationSteps.append(operationStep)

    print(totalCost)
    print (operationSteps)

    return totalCost


def test_time_taken():
    for i in range(10, 100, 10):
        testFibSeriesR = timeit.Timer(functools.partial(FibSeriesR, i), "from __main__ import FibSeriesR")
        fibSeriesRTime = testFibSeriesR.timeit(number=10)

        testFibSeriesI = timeit.Timer(functools.partial(FibSeriesI, i), "from __main__ import FibSeriesI")
        fibSeriesITime = testFibSeriesI.timeit(number=10)

        testFibSeriesM = timeit.Timer(functools.partial(FibSeriesM, i), "from __main__ import FibSeriesM")
        fibSeriesMTime = testFibSeriesM.timeit(number=10)
        print("%d, FibSeriesR = %f, FibSeriesI = %f, FibSeriesM = %f" % (
        i, fibSeriesRTime, fibSeriesITime, fibSeriesMTime))


def main():
    # print(factorialRecursion(5))

    # print(factorialRecursion(969))
    # print(reverseListRecursion([1,2,3,4,5,7,8,9,10,11,12,13,14,15]))

    # print(FibonacciR(20))
    print(FibSeriesR(20))

    # print(FibonacciI(20))
    print(FibSeriesI(20))

    fibDictionary = {1: 1, 0: 0}
    # print(FibonacciM(20))
    print(FibSeriesM(20))
    # test_time_taken()
    getMinCost("alligator", "algorithm", 5,20,20)
    getMinCost("alligator", "alligattor", 5,20,20)


if __name__ == "__main__":
    main()

'''
FibSeriesR - [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
FibSeriesI - [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
FibSeriesM - [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

10, FibSeriesR = 0.003767, FibSeriesI = 0.000404, FibSeriesM = 0.000765
20, FibSeriesR = 0.463499, FibSeriesI = 0.001007, FibSeriesM = 0.002026
30, FibSeriesR = 33.921311, FibSeriesI = 0.000459, FibSeriesM = 0.001008
40, FibSeriesR = 97926.794101, FibSeriesI = 0.002531, FibSeriesM = 0.005612
'''
