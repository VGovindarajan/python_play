# https://runestone.academy/runestone/static/pythonds/Recursion/ExploringaMaze.html
# Ideas from the above link
# Vijayarajan Govindarajan 2017
import random


def makeMaze(size):
    maze = []
    for i in range(size):
        newList = []
        for j in range(size):
            rand = random.randrange(0, 10)
            if rand > 4:
                newList.append(0)
            else:
                newList.append(1)
        maze.append(newList)
    return maze


def printMaze(maze):
    for i in range(len(maze)):
        row = maze[i]
        strVal = getStrMazeRow(row)
        print(str(i) + " " + strVal)


def getStrMazeRow(row):
    strVal = ""
    for i in range(len(row)):
        if row[i] == 1:
            strVal = strVal + "|X"
        else:
            strVal = strVal + "| "
    return strVal


def getStartingPosition(maze):
    mazeLen = len(maze)
    rowNum = mazeLen // 2
    colNum = mazeLen // 2
    while maze[rowNum][colNum] == 1 or isAtEdge(maze, [rowNum, colNum]):
        rowNum = random.randrange(0, mazeLen)
        colNum = random.randrange(0, mazeLen)
    return [rowNum, colNum]


def isAtEdge(maze, position):
    mazeLen = len(maze)
    rowNum = position[0]
    colNum = position[1]
    if rowNum == 0 or colNum == 0:
        return True
    if rowNum == mazeLen - 1 or colNum == mazeLen - 1:
        return True
    return False


def canVisit(maze, position):
    retVal = maze[position[0]][position[1]] is 0
    #print("can visit", position, retVal)
    return retVal

def alreadyVisited(visitedList, position):
    visited = False
    visitedLen = len(visitedList)
    #print("already visit", position, visitedLen)
    for i in range(visitedLen):
        pos = visitedList[i]
        #print(i, pos)
        if pos[0] == position[0] and pos[1] == position[1]:
            visited = True
            #print(visitedList, position)
            break
    #print("already visit", position, visited)
    return visited


def escapeFromMaze(maze, visitedList, startPos):
    print("In Maze", visitedList, startPos)
    escaped = False
    isEdge = isAtEdge(maze, startPos)
    if isEdge:
        print("Escaped ...")
        escaped = True
        return True
    visitedList.append(startPos)
    while not escaped:
        # Turn Left. Reduce one col
        newPos = [startPos[0], startPos[1] - 1]
        if canVisit(maze, newPos) and not alreadyVisited(visitedList, newPos):
            escaped = escapeFromMaze(maze, visitedList, newPos)
            if escaped:
                return escaped
        # Go up. add one row
        newPos = [startPos[0] + 1, startPos[1]]
        if canVisit(maze, newPos) and not alreadyVisited(visitedList, newPos):
            escaped = escapeFromMaze(maze, visitedList, newPos)
            if escaped:
                return escaped
        # Go right. add one col
        newPos = [startPos[0], startPos[1] + 1]
        if canVisit(maze, newPos) and not alreadyVisited(visitedList, newPos):
            escaped = escapeFromMaze(maze, visitedList, newPos)
            if escaped:
                return escaped
        # Go down. reduce one row
        newPos = [startPos[0] - 1, startPos[1]]
        if canVisit(maze, newPos) and not alreadyVisited(visitedList, newPos):
            escaped = escapeFromMaze(maze, visitedList, newPos)
            if escaped:
                return escaped
        print("Loop again ", startPos, visitedList)
        return False


def main():
    maze = makeMaze(12)
    printMaze(maze)
    startPos = getStartingPosition(maze)
    print(startPos)
    #print(isAtEdge(maze, startPos))
    escaped = escapeFromMaze(maze, [], startPos)
    print("Escaped ", escaped)

if __name__ == "__main__":
    main()

('\n'
 'C:\Python34\python.exe C:/Work/python/python_play/algorithms/mazeRunner.py\n'
 '0 |X|X|X|X| |X| | | | |X| \n'
 '1 | |X|X| | |X|X|X| | |X| \n'
 '2 |X|X| | |X| |X| | | |X|X\n'
 '3 |X| | |X| |X|X|X| | |X|X\n'
 '4 | | | |X|X|X|X| | | | | \n'
 '5 |X|X| |X| | |X| | |X| |X\n'
 '6 |X|X| | |X|X|X|X| | |X| \n'
 '7 | |X| | | | |X| |X|X|X| \n'
 '8 |X|X|X| |X| |X|X|X| |X|X\n'
 '9 | | |X| | |X|X| | | |X| \n'
 '10 | |X|X|X|X|X| | |X| |X| \n'
 '11 | | | |X|X| | |X| |X|X| \n'
 '[7, 5]\n'
 'False\n'
 'In Maze [] [7, 5]\n'
 'In Maze [[7, 5]] [7, 4]\n'
 'In Maze [[7, 5], [7, 4]] [7, 3]\n'
 'In Maze [[7, 5], [7, 4], [7, 3]] [7, 2]\n'
 'In Maze [[7, 5], [7, 4], [7, 3], [7, 2]] [6, 2]\n'
 'In Maze [[7, 5], [7, 4], [7, 3], [7, 2], [6, 2]] [6, 3]\n'
 'Loop again  [6, 3] [[7, 5], [7, 4], [7, 3], [7, 2], [6, 2], [6, 3]]\n'
 'In Maze [[7, 5], [7, 4], [7, 3], [7, 2], [6, 2], [6, 3]] [5, 2]\n'
 'In Maze [[7, 5], [7, 4], [7, 3], [7, 2], [6, 2], [6, 3], [5, 2]] [4, 2]\n'
 'In Maze [[7, 5], [7, 4], [7, 3], [7, 2], [6, 2], [6, 3], [5, 2], [4, 2]] [4, 1]\n'
 'In Maze [[7, 5], [7, 4], [7, 3], [7, 2], [6, 2], [6, 3], [5, 2], [4, 2], [4, 1]] [4, 0]\n'
 'Escaped ...\n'
 'Escaped  True\n'
 'Process finished with exit code 0\n')

('\n'
 'C:\Python34\python.exe C:/Work/python/python_play/algorithms/mazeRunner.py\n'
 '0 | |X|X| |X| |X| | |X| | \n'
 '1 | | |X|X| | |X|X| | | | \n'
 '2 | |X|X| | | |X| | |X|X| \n'
 '3 | | | |X| | | |X|X| |X| \n'
 '4 |X| | |X|X|X|X| | |X|X| \n'
 '5 | |X|X| | |X| |X| |X| | \n'
 '6 | | |X| | |X|X|X| | |X| \n'
 '7 | |X|X|X| | |X| |X| |X|X\n'
 '8 |X| |X|X| |X|X|X| |X| | \n'
 '9 |X| | |X| |X| | |X| |X| \n'
 '10 |X| | | |X|X| |X| | |X|X\n'
 '11 | |X| | |X| | |X|X| | |X\n'
 '[7, 9]\n'
 'In Maze [] [7, 9]\n'
 'In Maze [[7, 9]] [6, 9]\n'
 'In Maze [[7, 9], [6, 9]] [6, 8]\n'
 'In Maze [[7, 9], [6, 9], [6, 8]] [5, 8]\n'
 'In Maze [[7, 9], [6, 9], [6, 8], [5, 8]] [4, 8]\n'
 'In Maze [[7, 9], [6, 9], [6, 8], [5, 8], [4, 8]] [4, 7]\n'
 'Loop again  [4, 7] [[7, 9], [6, 9], [6, 8], [5, 8], [4, 8], [4, 7]]\n'
 'Loop again  [4, 8] [[7, 9], [6, 9], [6, 8], [5, 8], [4, 8], [4, 7]]\n'
 'Loop again  [5, 8] [[7, 9], [6, 9], [6, 8], [5, 8], [4, 8], [4, 7]]\n'
 'Loop again  [6, 8] [[7, 9], [6, 9], [6, 8], [5, 8], [4, 8], [4, 7]]\n'
 'Loop again  [6, 9] [[7, 9], [6, 9], [6, 8], [5, 8], [4, 8], [4, 7]]\n'
 'Loop again  [7, 9] [[7, 9], [6, 9], [6, 8], [5, 8], [4, 8], [4, 7]]\n'
 'Escaped  False\n'
 '\n'
 'Process finished with exit code 0\n')