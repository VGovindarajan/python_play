# https://runestone.academy/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
# Vijayarajan Govindarajan 2017

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

from Node import Node


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

    def insert(self, pos, item):
        invalidPosition = -1
        size = self.size()
        if size < pos:
            # print("LinkedList size is ", size, " cannot insert at ",  pos)
            return invalidPosition
        current = self.head
        previous = None
        position = 0
        while current is not None and pos != position:
            previous = current
            current = current.getNext()
            position += 1

        node = Node(item)
        node.setNext(current)
        if previous is None:
            self.head = node
        else:
            previous.setNext(node)

        return position

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
    u = UnorderedListImpl()
    u.add(111)
    u.add(222)
    u.add(333)

    print(u)
    print(u.isEmpty)
    print(u.size())

    print("is 122 available ?", u.search(122))
    print("index of 122 ?", u.index(122))
    print("Removed first 122 if available ?", u.remove(122))

    print("is 222 available ?", u.search(222))
    print("index of 222 ?", u.index(222))
    # print(u[1])
    print("Removed first 222 if available ?", u.remove(222))

    print(u)

    u.append(444)

    print(u)

    ul = UnorderedListImpl()
    print("pop() on new list", ul.pop())
    ul.append(555)
    ul.insert(3, 111)
    ul.insert(0, 222)
    ul.insert(1, 333)
    ul.insert(3, 444)
    ul.insert(0, "baa")
    print(ul)

    print("pop at index 7", ul.pop(7))
    print("pop at index 0", ul.pop(0))
    print(ul)
    print("pop at index 3", ul.pop(3))
    print(ul)
    print("pop() on list", ul.pop())
    print(ul)


if __name__ == "__main__":
    main()
