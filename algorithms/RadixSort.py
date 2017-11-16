#https://runestone.academy/runestone/static/pythonds/BasicDS/ProgrammingExercises.html, #10
# Vijayarajan Govindarajan 2017

from QueueImpl import QueueImpl

integers = (0,1,2,3,4,5,6,7,8,9)


def radixSort(listOfItems, *args):
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
        if lenJ -1 >= position:
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
        #print("sorting ", returnList, position+1 )
        return radixSort(returnList, position+1)
    else:
        #print("Returning ", returnList )
        return returnList



def main():
    inputList = [12, 32, 23, 44, 56, 65, 349, 1, 0, 12, 11, 1, 0, 45, 56, 65, 349, 301, 129, 34]
    print(inputList)
    radixSortOutput = radixSort(inputList)
    print(radixSortOutput)

if __name__ == "__main__":
    main()
