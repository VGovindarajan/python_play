# https://runestone.academy/runestone/static/pythonds/BasicDS/ProgrammingExercises.html
# Vijayarajan Govindarajan 2017

'''
The linked list implementation given above is called a singly linked list
because each node has a single reference to the next node in sequence.
 An alternative implementation is known as a doubly linked list. In this
 implementation, each node has a reference to the next node
 (commonly called next) as well as a reference to the preceding node
  (commonly called back). The head reference also contains two references,
   one to the first node in the linked list and one to the last. Code this
    implementation in Python.

DoublyLinkedList() creates a new list that is empty. It needs no parameters and returns an empty list.
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


class DoublyLinkedListImpl:

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return "head :" + str(self.head)

    def add(self, item):
        n = Node(item)
        n.setNext(self.head)
        currentHead = self.head
        n.setBack(None)
        self.head = n
        if self.tail is None:
            self.tail = n
        if currentHead is not None:
            currentHead.setBack(n)

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
        found = False

        while not found and current is not None:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        if found:
            if current == self.head:
                self.head = current.getNext()
                if current == self.tail:
                    self.tail = None

            if current == self.tail:
                self.tail = current.getBack()
                self.tail.setNext(None)

            prev = current.getBack()
            if prev is not None and prev is not self.tail:
                prev.setNext(current.getNext())

        return found

    def append(self, item):
        if self.head is None and self.tail is None:
            return self.add(item)

        current = self.tail
        n = Node(item)
        n.setBack(current)
        n.setNext(None)
        current.setNext(n)
        self.tail = n

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
        position = 0
        while current is not None and pos != position:
            current = current.getNext()
            position += 1

        if current is None:
            return self.append(item)

        previous = current.getBack()
        node = Node(item)
        node.setNext(current)
        if previous is None:
            self.head = node
        else:
            previous.setNext(node)

        if current == self.tail:
            self.tail = node

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

        previous = None
        if pos == (size-1):
            current = self.tail
            if current is not None:
                previous = current.getBack()
            if previous is not None:
                previous.setNext(None)
            self.tail = previous
            if current is not None:
                return current.getData()

        current = self.head
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

    def isEmpty(self):
        return self.head is None

def test_1():
    d = DoublyLinkedListImpl()
    d.append(0)
    d.add(1)
    d.add(2)
    d.add(3)
    d.add(4)
    d.add(5)
    print(d)

    print(d.size())
    d.insert(d.size(),"New Tail")
    d.insert(2,"At 2nd index")
    d.insert(0, "At 0 index")

    print(d)

    print("Remove 3", d.remove(3))
    print(d)
    print("Remove 5 (head)", d.remove(5))
    print(d)
    print("Remove 1 (tail)", d.remove(1))
    print(d)

    d.append(1)
    print(d)
    print(d.tail)

    dd = DoublyLinkedListImpl()
    while not d.isEmpty():
        pp = d.pop()
        print(pp)
        if pp is not None:
            dd.add(pp)
    print("-----------------")
    while not dd.isEmpty():
        pp = dd.pop(0)
        print(pp)




def main():
    test_1()

if __name__ == "__main__":
    main()