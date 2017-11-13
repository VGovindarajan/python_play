#https://runestone.academy/runestone/static/pythonds/BasicDS/ImplementingaDequeinPython.html
#Vijayarajan Govindarajan 2017

class DequeImpl:
    def __init__(self):
        self.items = []

    def __repr__(self):
        retVal = ""
        for i in self.items:
            retVal += (str(i) + " ")
        return retVal

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addFront(self, item):
        self.items.append(item)

    def addBack(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)


def palindromeChecker(strToCheck):
    deq = DequeImpl()

    for ch in strToCheck:
        deq.addBack(ch)

    stillEqual = True

    while deq.size() > 1 and stillEqual:
        front = deq.removeFront()
        rear = deq.removeRear()
        if front != rear:
            stillEqual = False
    return stillEqual


def main():
    d = DequeImpl()
    d.addFront(1)
    d.addFront("True")
    d.addBack(23.34)
    print(d)
    while not d.isEmpty():
        print(str(d.removeFront()))

    pa1 = "MadaM"
    pa2 = "AmmA"
    pa3 = "Malayalam"
    pa4 = "malayalam"
    pa5 = "radar"

    print(pa1, " is a palindrome ? ", palindromeChecker(pa1))
    print(pa2, " is a palindrome ? ", palindromeChecker(pa2))
    print(pa3, " is a palindrome ? ", palindromeChecker(pa3))
    print(pa4, " is a palindrome ? ", palindromeChecker(pa4))
    print(pa5, " is a palindrome ? ", palindromeChecker(pa5))


if __name__ == "__main__":
    main()