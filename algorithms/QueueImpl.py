#https://runestone.academy/runestone/static/pythonds/BasicDS/ImplementingaQueueinPython.html
# Vijayarajan Govindarajan 2017

class QueueImpl:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def deque(self):
        return self.items.pop()

    def __repr__(self):
        retVal = ""
        for i in self.items:
            retVal = str(i) + " " + retVal
        return retVal


def main():
    queue = QueueImpl()
    queue.enqueue(1)
    queue.enqueue("True")
    queue.enqueue(23.34)
    print(queue)
    while not queue.isEmpty():
        print(str(queue.deque()))

    names = ["Apple", "Boy", "Charlie", "David", "Eagle", "Friend", "Gamma", "Harry", "India"]
    lastOneFor7 = hotPotatoes(names, 7)
    print(names, " last one for 7", lastOneFor7)
    lastOneFor5 = hotPotatoes(names, 5)
    print(names, " last one for 5", lastOneFor5)

def hotPotatoes(nameList, num):
    simQueue = QueueImpl()
    for name in nameList:
        simQueue.enqueue(name)

    while simQueue.size() > 1:
        for i in range(num):
            simQueue.enqueue(simQueue.deque())

        removed = simQueue.deque()
       # print("Removed %s, Queue Size is %d" %(removed, simQueue.size()))

    return simQueue.deque()

if __name__ == "__main__":
    main()