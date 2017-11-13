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

def main():
    d = DequeImpl()
    d.addFront(1)
    d.addFront("True")
    d.addBack(23.34)
    print(d)
    while not d.isEmpty():
        print(str(d.removeFront()))

if __name__ == "__main__":
    main()