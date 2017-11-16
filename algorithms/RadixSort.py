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

    for j in listOfItems:
        divisor = (10**position) * 10
        if divisor == 0:
            divisor = 1

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
        print("str impl ", t4.timeit(number=100), "milliseconds")


'''
1000
int impl  1.889598973342563 milliseconds
str impl  1.8513608494860438 milliseconds
2000
int impl  6.744180671638018 milliseconds
str impl  7.170844494925824 milliseconds
3000
int impl  12.620656007036985 milliseconds
str impl  11.496835220493008 milliseconds
4000
int impl  14.069975249679452 milliseconds
str impl  8.86378466650929 milliseconds
5000
int impl  19.056839067417343 milliseconds
str impl  15.396405026394376 milliseconds
6000
int impl  16.599875012971964 milliseconds
str impl  22.25017210424862 milliseconds
7000
int impl  30.86031635250754 milliseconds
str impl  19.807096891175746 milliseconds
8000
int impl  13.356388650356763 milliseconds
str impl  18.820905144805153 milliseconds
9000
int impl  36.884047162076 milliseconds
str impl  37.07878858375784 milliseconds

Process finished with exit code 0
'''

if __name__ == "__main__":
    main()
