#https://runestone.academy/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
#Vijayarajan Govindarajan 2017

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def __repr__(self):
        return str(self.data) + " " + str(self.next)

def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.setNext(n2)
    n2.setNext(n3)

    print(n1)
    print(n2)

if __name__ == "__main__":
    main()