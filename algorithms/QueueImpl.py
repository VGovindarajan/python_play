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

if __name__ == "__main__":
    main()