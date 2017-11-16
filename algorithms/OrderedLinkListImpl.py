# https://runestone.academy/runestone/static/pythonds/BasicDS/TheOrderedListAbstractDataType.html
# Vijayarajan Govindarajan 2017
# Based on LinkedListImpl.py

'''
OrderedList() creates a new ordered list that is empty. It needs no parameters and returns an empty list.
add(item) adds a new item to the list making sure that the order is preserved. It needs the item and returns nothing. Assume the item is not already in the list.
remove(item) removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.
search(item) searches for the item in the list. It needs the item and returns a boolean value.
isEmpty() tests to see whether the list is empty. It needs no parameters and returns a boolean value.
size() returns the number of items in the list. It needs no parameters and returns an integer.
index(item) returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.
pop() removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.
pop(pos) removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.
'''

from Node import Node


class OrderedLinkListImpl:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return str(self.head)

    def isEmpty(self):
        return True if self.head is None else False

    def add(self, data):
        previous = None
        current = self.head
        stop = False

        while current is not None and stop is False:
            if current.getData() > data:
                stop = True
            else:
                previous = current
                current = current.getNext()

        n = Node(data)

        if previous is None:
            n.setNext(self.head)
            self.head = n
        else:
            n.setNext(current)
            previous.setNext(n)

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
        stop = False
        while current is not None and found is not True and stop is not True:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
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

    def index(self, item):
        current = self.head
        found = False
        invalidPosition = -1
        position = 0
        while current is not None and found is not True:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                position += 1

        if found is True:
            return position
        else:
            return invalidPosition

    def pop(self, *args):
        invalidPosition = -1
        size = self.size()
        pos = size - 1
        if len(args) == 1 and isinstance(args[0], int):
            pos = args[0]

        if size - 1 < pos:
            print("LinkedList index positions are from 0 To ", size - 1, " cannot pop at ", pos)
            return invalidPosition
        current = self.head
        previous = None
        position = 0
        while current is not None and pos != position:
            previous = current
            current = current.getNext()
            position += 1

        if previous is None and current is None:
            return
        elif previous is None and current is not None:
            self.head = current.getNext()
        elif previous is not None:
            previous.setNext(current.getNext())

        return current.getData()


def main():
    ol = OrderedLinkListImpl()
    ol.add(120)
    ol.add(220)
    ol.add(12)
    ol.add(1)

    print(ol)

    print("search(220)", ol.search(220))
    print(ol)
    print("search(234)", ol.search(234))
    print(ol)

    print("pop()", ol.pop())
    print(ol)
    print("pop(2)", ol.pop(2))
    print(ol)

    print("index(1)", ol.index(1))
    print(ol)

    print("remove(220)", ol.remove(220))
    print(ol)
    print("remove(12)", ol.remove(12))
    print(ol)


if __name__ == "__main__":
    main()
