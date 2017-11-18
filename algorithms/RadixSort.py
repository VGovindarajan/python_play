# https://runestone.academy/runestone/static/pythonds/BasicDS/ProgrammingExercises.html, #10
# Vijayarajan Govindarajan 2017

import functools
import random
import timeit

from QueueImpl import QueueImpl

integers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


def radixSortStrImpl(listOfItems, *args):
    position = 0
    if len(args) == 1:
        position = int(args[0])
    stillSorting = False
    dicQueues = {}
    for i in integers:
        q = QueueImpl()
        dicQueues[str(i)] = q

    otherQ = QueueImpl()

    for j in listOfItems:
        strJ = str(j)
        lenJ = len(strJ)
        if lenJ - 1 >= position:
            posJ = lenJ - 1 - position
            index = strJ[posJ]
            dicQueues[index].enqueue(j)
            stillSorting = True
        else:
            otherQ.enqueue(j)

    returnList = []

    while not otherQ.isEmpty():
        returnList.append(int(otherQ.deque()))

    for i in integers:
        while not dicQueues[str(i)].isEmpty():
            returnList.append(int(dicQueues[str(i)].deque()))

    if stillSorting is True:
        # print("sorting ", returnList, position+1 )
        return radixSortStrImpl(returnList, position + 1)
    else:
        # print("Returning ", returnList )
        return returnList


def radixSortIntImpl(listOfItems, *args):
    position = 0
    if len(args) == 1:
        position = int(args[0])
    stillSorting = False
    dicQueues = {}
    for i in integers:
        q = QueueImpl()
        dicQueues[i] = q

    otherQ = QueueImpl()

    divisor = (10**position) * 10
    if divisor == 0:
        divisor = 1

    for j in listOfItems:
        #print("j", j, "position", position)
        if j >= divisor:
            result = j // divisor
            modulus = result % 10
            dicQueues[modulus].enqueue(j)
            stillSorting = True
        else:
            otherQ.enqueue(j)

    returnList = []

    while not otherQ.isEmpty():
        returnList.append(otherQ.deque())

    for i in integers:
        while not dicQueues[i].isEmpty():
            returnList.append(dicQueues[i].deque())

    if stillSorting is True:
        # print("sorting ", returnList, position+1 )
        return radixSortIntImpl(returnList, position + 1)
    else:
        # print("Returning ", returnList )
        return returnList


def GetListOfSizeN(size):
    return random.sample(range(100000), size)


def runStrImpl(inputList):
    #print(inputList)
    radixSortStrImplOutput = radixSortStrImpl(inputList)
    #print(radixSortStrImplOutput)

def runIntImpl(inputList):
    #print(inputList)
    radixSortStrImplOutput = radixSortStrImpl(inputList)
    #print(radixSortStrImplOutput)



A = 1


def main():
    for i in range(1000, 10000, 1000):
        A = i
        inputList = GetListOfSizeN(i)
        print(i)
        t4 = timeit.Timer(functools.partial(radixSortIntImpl, inputList), "from __main__ import radixSortIntImpl")
        print("int impl ", t4.timeit(number=100), "milliseconds")

        t5 = timeit.Timer(functools.partial(radixSortStrImpl, inputList), "from __main__ import radixSortStrImpl")
        print("str impl ", t5.timeit(number=100), "milliseconds")


'''
1000
int impl  0.976603705591687 milliseconds
str impl  2.0103175119066488 milliseconds
2000
int impl  1.9697028098893323 milliseconds
str impl  4.209769895384185 milliseconds
3000
int impl  3.1947729725435288 milliseconds
str impl  6.789623035626246 milliseconds
4000
int impl  4.340705211175997 milliseconds
str impl  8.725804765548592 milliseconds
5000
int impl  5.79279902899372 milliseconds
str impl  24.870661613967222 milliseconds
6000
int impl  19.43445042390293 milliseconds
str impl  32.716978507020826 milliseconds
7000
int impl  15.7413152451863 milliseconds
str impl  28.2207028391594 milliseconds
8000
int impl  10.18594481336146 milliseconds
str impl  19.753194714812537 milliseconds
9000
int impl  17.83018261866829 milliseconds
str impl  26.86114199674381 milliseconds

Process finished with exit code 0
'''

if __name__ == "__main__":
    main()
