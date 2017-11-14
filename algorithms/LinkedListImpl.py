#https://runestone.academy/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
#Vijayarajan Govindarajan 2017

'''
List() creates a new list that is empty. It needs no parameters and returns an empty list.
add(item) adds a new item to the list. It needs the item and returns nothing. Assume the item is not already in the list.
remove(item) removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.
search(item) searches for the item in the list. It needs the item and returns a boolean value.
isEmpty() tests to see whether the list is empty. It needs no parameters and returns a boolean value.
size() returns the number of items in the list. It needs no parameters and returns an integer.
append(item) adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list.
index(item) returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.
insert(pos,item) adds a new item to the list at position pos. It needs the item and returns nothing. Assume the item is not already in the list and there are enough existing items to have position pos.
pop() removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.
pop(pos) removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.
'''

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

class UnorderedListImpl:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return str(self.head)

    def isEmpty(self):
        return True if self.head is None else False

    def add(self, data):
        n = Node(data)
        n.setNext(self.head)
        self.head = n

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and found is not True:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found and current is not None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if found:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

        return found

    def append(self, item):
        current = self.head
        previous = None

        while current is not None:
            previous = current
            current = current.getNext()

        n = Node(item)

        if previous is None:
            self.head = n
        else:
            previous.setNext(n)


def main():
    #n1 = Node(1)
    #n2 = Node(2)
    #n3 = Node(3)
    #n1.setNext(n2)
    #n2.setNext(n3)

    #print(n1)
    #print(n2)

    u = UnorderedListImpl()
    u.add(111)
    u.add(222)
    u.add(333)

    print(u)
    print(u.isEmpty())
    print(u.size())

    print("is 122 available ?", u.search(122))
    print("Removed first 122 if available ?", u.remove(122))

    print("is 222 available ?", u.search(222))
    print("Removed first 222 if available ?", u.remove(222))

    print(u)

    u.append(444)

    print(u)

    ul = UnorderedListImpl()
    ul.append(555)
    print(ul)

if __name__ == "__main__":
    main()