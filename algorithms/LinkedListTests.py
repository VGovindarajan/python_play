from DoublyLinkedListImpl import DoublyLinkedListImpl
from LinkedListImpl import UnorderedListImpl

import functools

import timeit


def addTest(count):
    d = UnorderedListImpl()
    for i in range(count):
        d.add(i)

def appendTest(count):
    d = UnorderedListImpl()
    for i in range(count):
        d.append(i)


def main():
    for i in range(1000, 10000, 1000):

        t4 = timeit.Timer(functools.partial(addTest, i), "from __main__ import addTest")
        addTime =  t4.timeit(number=10)

        t5 = timeit.Timer(functools.partial(appendTest, i), "from __main__ import appendTest")
        appendTime = t5.timeit(number=10)
        print("%d, addTime = %f, appendTime = %f" %(i, addTime, appendTime))

if __name__ == "__main__":
    main()

'''
DoublyLinkedListImpl
100000, addTime = 2.679434, appendTime = 2.368185
200000, addTime = 8.501625, appendTime = 8.422688
300000, addTime = 11.333085, appendTime = 8.561667
400000, addTime = 13.118393, appendTime = 13.440202
500000, addTime = 14.949485, appendTime = 14.256775
600000, addTime = 30.578508, appendTime = 28.494290
700000, addTime = 25.008215, appendTime = 25.142511
800000, addTime = 25.668967, appendTime = 28.513711
900000, addTime = 28.973625, appendTime = 31.910007

Process finished with exit code 0
'''