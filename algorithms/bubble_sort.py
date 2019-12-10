#https://runestone.academy/runestone/static/pythonds/SortSearch/TheBubbleSort.html
## Vijayarajan Govindarajan 2017

def bubbleSort(anyList):
    listLen = len(anyList)
    for run_num in range(listLen-1,0,-1):
        #print(run_num)
        for i in range(run_num):
            #print(i, anyList[i], anyList[i+1] )
            if anyList[i] > anyList[i+1]:
                temp = anyList[i]
                anyList[i] = anyList[i+1]
                anyList[i+1] = temp

    return anyList


def shortBubbleSort(anyList):
    listLen = len(anyList)
    flipped_this_run = True

    for run_num in range(listLen-1,0,-1):
        while flipped_this_run:
            print(run_num)
            flipped_this_run = False
            for i in range(run_num):
                print(i, anyList[i], anyList[i+1] )
                if anyList[i] > anyList[i+1]:
                    temp = anyList[i]
                    anyList[i] = anyList[i+1]
                    anyList[i+1] = temp
                    flipped_this_run = True

    return anyList

def main():
    testList = [1,2,12,1,45,21,34,6,46,8,9,34]
    print(testList)
    bubbleSort(testList)
    print(testList)
    shortBubbleSort(testList)
    print(testList)
if __name__ =="__main__":
    main()
