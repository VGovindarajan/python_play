#https://runestone.academy/runestone/static/pythonds/SortSearch/TheBinarySearch.html
# Vijayarajan Govindarajan 2017

def binary_search(sortedList, itemToSearch):
    #print("find", itemToSearch, " in", sortedList)
    first = 0
    last = len(sortedList)-1
    found = False

    while first <= last and found is False:

        mid = (first + last)//2
        midElem = sortedList[mid]
        #print("first index :", first, "last index :", last,"mid index: ", mid, "midElement", midElem)

        if midElem == itemToSearch:
            found = True
        else:
            if midElem > itemToSearch:
                last = mid-1
            else:
                first = mid+1
    #if found:
        #print(itemToSearch,  " found  in ", sortedList)
    #else:
        #print(itemToSearch,  " not  in ", sortedList)

    return found

def main():
    listOfNum = [1,3,5,7,9,11,15, 17, 18, 19, 21, 23, 24, 25, 26, 27, 28,29,31,33,34]
    fiveFound = binary_search(listOfNum, 5)
    sixfound = binary_search(listOfNum, 6)
    print(fiveFound, sixfound)

if __name__ == "__main__":
    main()

