# Vijayarajan Govindarajan 2017
'''
from StackImpl import StackImpl

t1 = StackImpl()
t1.setName("From ")
t2 = StackImpl()
t2.setName("To ")
t3 = StackImpl()
t3.setName("With ")

discs =[3,2,1]


def move(height, fromTower, toTower):
    item = fromTower.pop()
    peekItem = None
    if not toTower.isEmpty():
        peekItem = toTower.peek()
    if peekItem is not None and peekItem <= height:
        raise ValueError('Trying to add a bigger disk ...')

    print("Moving ", height, " from ", fromTower, " to ", toTower )
    toTower.push(height)
    #moveCount +=1
    print(toTower)

def moveTower(height, fromTower, toTower, withTower):
    print("moveTower", height)
    if height >= 1:
        moveTower(height-1, fromTower, withTower, toTower)
        move([height], fromTower, toTower)
        moveTower(height-1, withTower, toTower, fromTower)


def main():
    moveCount = 0
    moveTower(3, t1, t2,t3)
    print(moveCount)
'''

tower1 = []
tower2 = []
tower3 = []

def moveDisc(discHeight, fromTower, toTower):
    disc = None
    if len(fromTower) > 0:
        disc = fromTower.pop()
    if disc is None:
        disc = discHeight
    toTower.append(disc)
    print(toTower)

def towerOfHanoi(height, fromTower, toTower, withTower):
    if height >= 1:
        towerOfHanoi(height-1, fromTower, withTower, toTower)
        moveDisc(height, fromTower, toTower)
        towerOfHanoi(height-1, withTower, toTower, fromTower)

def main():
    towerOfHanoi(5, tower1, tower2, tower3)
    print(tower2)

if __name__ == "__main__":
    main()