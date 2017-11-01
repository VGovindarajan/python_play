# Vijayarajan Govindarajan 2017
# http://www.sudokukingdom.com/
# http://www.sudokukingdom.com/very-easy-sudoku.php
import datetime as dt

newline = '\n'
allowedNumbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
allowedColsRows = (0, 1, 2, 3, 4, 5, 6, 7, 8)
zero = 0
nine = 9
eightyone =81

def getColSeparator(index):
    if (index > 0) & ((index % 3) == 0) & ((index % 9) != 0):
        return " | "
    return ""

def getRowSeparator(index):
    if (index > 0) & ((index % 3) == 0) & ((index % 9) != 0):
        return "-" * 33 + newline
    return ""

def getEmptyGrid(rows, cols):
    grid = [[] for i in range(rows)]
    for i in range(0, cols):
        for j in range(0, rows):
            value = (i * cols) + j
            grid[i].append(zero)
    return grid

def getHomeSquareStart(index):
    # 0-2, 3-5, 6-8
    if index not in allowedColsRows:
        return None
    floordivThree = index // 3
    return floordivThree * 3

def getHomeSquareEnd(index):
    # 0-2, 3-5, 6-8
    if index not in allowedColsRows:
        return None
    floordivThree = index // 3
    return ((floordivThree + 1) * 3)

class Sudoku:
    def __init__(self, name):
        self.name = name
        self.grid = getEmptyGrid(9, 9)

    def __repr__(self):
        printgrid = ''
        for i in range(0, 9):
            printgrid = printgrid + newline + getRowSeparator(i)
            for j in range(0, 9):
                index = (i * 9) + j
                colSep = getColSeparator(index)
                printgrid = printgrid + colSep + '{:>3}'.format(self.grid[i][j])
        printgrid = printgrid + newline
        return self.name + printgrid

    def copyGrid(self):
        newGrid = getEmptyGrid(9, 9)
        for i in allowedColsRows:
            for j in allowedColsRows:
                newGrid[i][j] = self.grid[i][j]
        return newGrid

    def assignGrid(self, grid):
        for i in allowedColsRows:
            for j in allowedColsRows:
                self.grid[i][j] = grid[i][j]
        return

    def addAtIndexPosition(self, rowIndex, colIndex, value):
        self.addAtPosition(rowIndex + 1, colIndex + 1, value)
        return self

    # User input. Reduce 1 to get actual index for row and column
    def addAtPosition(self, rowNum, colNum, value):
        rowIndex = rowNum - 1
        colIndex = colNum - 1
        valueToChange = value

        if not valueToChange in allowedNumbers:
            return
        if not rowIndex in allowedColsRows:
            return

        possibleNumbersInRow = self.getPossibleNumbersInRow(rowIndex)
        if not valueToChange in possibleNumbersInRow:
            return
        if not colIndex in allowedColsRows:
            return

        possibleNumbersInCol = self.getPossibleNumbersInCol(colIndex)
        if not valueToChange in possibleNumbersInCol:
            return

        rowInQuestion = self.grid[rowIndex]
        rowInQuestion[colIndex] = valueToChange
        self.grid[rowIndex] = rowInQuestion
        return self

    def getNumbersInRow(self, rowIndex):
        rowInQuestion = self.grid[rowIndex]
        retVal = []
        for i in rowInQuestion:
            if i in allowedNumbers:
                retVal.append(i)
        return retVal

    def getPossibleNumbersInRow(self, rowIndex):
        numbersInRow = self.getNumbersInRow(rowIndex)
        return tuple((set(allowedNumbers).difference(numbersInRow)))

    def getUnfilledIndicesInRow(self, rowIndex):
        rowInQuestion = self.grid[rowIndex]
        retVal = []
        for i in allowedColsRows:
            if rowInQuestion[i] not in allowedNumbers:
                retVal.append([rowIndex, i])
        return retVal

    def getNumbersInCol(self, colIndex):
        retVal = []
        for i in allowedColsRows:
            rowInQuestion = self.grid[i]
            if rowInQuestion[colIndex] in allowedNumbers:
                retVal.append(rowInQuestion[colIndex])
        return retVal

    def getPossibleNumbersInCol(self, colIndex):
        numbersInCol = self.getNumbersInCol(colIndex)
        return tuple((set(allowedNumbers).difference(numbersInCol)))

    def getUnfilledIndicesInCol(self, colIndex):
        retVal = []
        for i in allowedColsRows:
            rowInQuestion = self.grid[i]
            if rowInQuestion[colIndex] not in allowedNumbers:
                retVal.append([i, colIndex])
        return retVal

    def getNumbersInHomeSquare(self, rowIndex, colIndex):
        retVal = []
        rowStartIndex = getHomeSquareStart(rowIndex)
        rowEndIndex = getHomeSquareEnd(rowIndex)
        colStartIndex = getHomeSquareStart(colIndex)
        colEndIndex = getHomeSquareEnd(colIndex)

        for i in range(rowStartIndex, rowEndIndex):
            rowInQuestion = self.grid[i]
            for j in range(colStartIndex, colEndIndex):
                if rowInQuestion[j] in allowedNumbers:
                    retVal.append(rowInQuestion[j])
        return retVal

    def getPossibleNumbersInHomeSquare(self, rowIndex, colIndex):
        numbersInHomeSquare = self.getNumbersInHomeSquare(rowIndex, colIndex)
        return tuple((set(allowedNumbers).difference(numbersInHomeSquare)))

    def getUnfilledRowColIndicesInHomeSquare(self, rowIndex, colIndex):
        retVal = []
        rowStartIndex = getHomeSquareStart(rowIndex)
        rowEndIndex = getHomeSquareEnd(rowIndex)
        colStartIndex = getHomeSquareStart(colIndex)
        colEndIndex = getHomeSquareEnd(colIndex)

        for i in range(rowStartIndex, rowEndIndex):
            rowInQuestion = self.grid[i]
            for j in range(colStartIndex, colEndIndex):
                if rowInQuestion[j] not in allowedNumbers:
                    retVal.append([i, j])
        return retVal

    def countNumberOfTimesNumberCanBePlacedInHomeSquare(self, numberToCheck, unfilledSquares):
        allowedCount = 0
        for i in unfilledSquares:
            rowIndex = i[0]
            colIndex = i[1]
            possibleNumbersInRow = self.getPossibleNumbersInRow(rowIndex)
            possibleNumbersInCol = self.getPossibleNumbersInCol(colIndex)
            numList = [numberToCheck]
            rowPossibilities = set(numList).issubset(set(possibleNumbersInRow))
            colPossibilities = set(numList).issubset(set(possibleNumbersInCol))
            if rowPossibilities & colPossibilities:
                allowedCount += 1
        return allowedCount

    def isSudokuSolved(self):
        for i in allowedColsRows:
            for j in allowedColsRows:
                if self.grid[i][j] == zero:
                    return False
        return True

    def getCountOfSquaresFilled(self):
        count = 0
        for i in allowedColsRows:
            for j in allowedColsRows:
                if not self.grid[i][j] == zero:
                    count += 1
        return count

class SudokuSolver:
    def __init__(self):
        self.name = ""

    def getMostFilledRowAndUnfilledIndices(self, sudoku, skipList):
        rowMax = 0
        rowIndex = 0
        rowIndices = []
        for i in allowedColsRows:
            if not i in skipList:
                filledRows = sudoku.getNumbersInRow(i)
                if len(filledRows) > rowMax:
                    rowMax = len(filledRows)
                    rowIndex = i
                    rowIndices = sudoku.getUnfilledIndicesInRow(i)
        return [rowIndex, rowIndices]

    def getMostFilledColAndUnfilledIndices(self, sudoku, skipList):
        colMax = 0
        colIndex = 0
        colIndices = []
        for i in allowedColsRows:
            if not i in skipList:
                filledCols = sudoku.getNumbersInCol(i)
                if len(filledCols) > colMax:
                    colMax = len(filledCols)
                    colIndex = i
                    colIndices = sudoku.getUnfilledIndicesInCol(i)
        return [colIndex, colIndices]

    def fillUniqueNumberForRowCol(self, sudoku, rowIndex, colIndex):
        squaresFilled = 0
        possibleNumbersInRow = sudoku.getPossibleNumbersInRow(rowIndex)
        possibleNumbersInCol = sudoku.getPossibleNumbersInCol(colIndex)
        possibleNumbersInHomeSquare = sudoku.getPossibleNumbersInHomeSquare(rowIndex, colIndex)
        # print("fillUniqueNumberForRowCol. RowIndex =", rowIndex, ", ColIndex =", colIndex, ", possibleNumbersInRow = ",
        #      possibleNumbersInRow, ", possibleNumbersInCol = ", possibleNumbersInCol,
        #      " possibleNumbersInHomeSquare = ", possibleNumbersInHomeSquare)
        rowColPossibilities = tuple(set(possibleNumbersInRow).intersection(possibleNumbersInCol))
        rowColSquarePossibilities = tuple(set(rowColPossibilities).intersection(possibleNumbersInHomeSquare))
        # print("fillUniqueNumberForRowCol. RowIndex =", rowIndex, ", ColIndex =", colIndex,
        #      ", rowColSquarePossibilities = ", rowColSquarePossibilities)
        if len(rowColSquarePossibilities) == 1:
            # print('Unique Match found for rowIndex = ', rowIndex, ', colIndex ', colIndex, ', number is ', list(rowColSquarePossibilities)[0])
            sudoku.addAtIndexPosition(rowIndex, colIndex, list(rowColSquarePossibilities)[0])
            squaresFilled = 1
        elif len(rowColSquarePossibilities) > 1:
            # print('Non-Unique Match found for rowIndex = ', rowIndex, ', colIndex ', colIndex, ', number is ', list(rowColSquarePossibilities))
            homeSquareUnfilled = sudoku.getUnfilledRowColIndicesInHomeSquare(rowIndex, colIndex)
            possibilityWeights = []
            for j in rowColSquarePossibilities:
                weight = sudoku.countNumberOfTimesNumberCanBePlacedInHomeSquare(j, homeSquareUnfilled)
                possibilityWeights.append([weight, j])
            possibilityWeights.sort()
            #print("lowest weight", possibilityWeights[0], possibilityWeights[1])
            if possibilityWeights[0][0] == 1:
                sudoku.addAtIndexPosition(rowIndex, colIndex, possibilityWeights[0][1])
                squaresFilled = 1
                #print('Single weight found for rowIndex = ', rowIndex, ', colIndex ', colIndex, ', number is ', possibilityWeights[0][1])
        return squaresFilled

    def fillUniqueNumbersForRow(self, sudoku, rowIndex, rowUnfilled):
        squaresFilled = 0
        for i in rowUnfilled:
            colIndex = i[1]
            squaresFilled += self.fillUniqueNumberForRowCol(sudoku, rowIndex, colIndex)
        return squaresFilled

    def fillUniqueNumbersForCol(self, sudoku, colIndex, colUnfilled):
        squaresFilled = 0
        for i in colUnfilled:
            rowIndex = i[0]
            squaresFilled += self.fillUniqueNumberForRowCol(sudoku, rowIndex, colIndex)
        return squaresFilled

    def fillKnownNumbers(self, sudoku, maxLoops):
        loopAgain = True
        while (loopAgain):
            isSolved = sudoku.isSudokuSolved()
            if isSolved:
                print("fillKnownNumbers. Sudoku solved at maxLoop ", maxLoops)
                return
            # print("fillKnownNumbers, maxLoops left", maxLoops)
            maxLoops -= 1
            colsTried = []
            rowsTried = []
            for i in allowedColsRows:
                numberOfBoxesFilled = 0
                # print("In Row. Filled Squares =", numberOfBoxesFilled, ", Loop Count = ", i, self.sudoku)
                rowsWithMostFills = self.getMostFilledRowAndUnfilledIndices(sudoku, rowsTried)
                rowsTried.append(rowsWithMostFills[0])
                numberOfBoxesFilled += self.fillUniqueNumbersForRow(sudoku, rowsWithMostFills[0], rowsWithMostFills[1])

                # print("In Col. Filled Squares =", numberOfBoxesFilled, ", Loop Count = ", i, self.sudoku)
                colWithMostFills = self.getMostFilledColAndUnfilledIndices(sudoku, colsTried)
                colsTried.append(colWithMostFills[0])
                numberOfBoxesFilled += self.fillUniqueNumbersForCol(sudoku, colWithMostFills[0], colWithMostFills[1])
            if maxLoops == 0:
                loopAgain = False
                # endregion

    def fillNonUniqueNumberForRowCol(self, sudoku, rowIndex, colIndex):
        debugStr = str(rowIndex) + "-" + str(colIndex)
        squaresFilled = 0
        possibleNumbersInRow = sudoku.getPossibleNumbersInRow(rowIndex)
        possibleNumbersInCol = sudoku.getPossibleNumbersInCol(colIndex)
        possibleNumbersInHomeSquare = sudoku.getPossibleNumbersInHomeSquare(rowIndex, colIndex)
        rowColPossibilities = tuple(set(possibleNumbersInRow).intersection(possibleNumbersInCol))
        rowColSquarePossibilities = tuple(set(rowColPossibilities).intersection(possibleNumbersInHomeSquare))
        if len(rowColSquarePossibilities) == 1:
            sudoku.addAtIndexPosition(rowIndex, colIndex, list(rowColSquarePossibilities)[0])
            squaresFilled = 1
            # print('Unique found for rowIndex = ', rowIndex, ', colIndex ', colIndex, ', number is ', list(rowColSquarePossibilities)[0])
        elif len(rowColSquarePossibilities) > 1:
            homeSquareUnfilled = sudoku.getUnfilledRowColIndicesInHomeSquare(rowIndex, colIndex)
            possibilityWeights = []
            for j in rowColSquarePossibilities:
                weight = sudoku.countNumberOfTimesNumberCanBePlacedInHomeSquare(j, homeSquareUnfilled)
                possibilityWeights.append([weight, j])
            possibilityWeights.sort()
            if possibilityWeights[0][0] == 1:
                sudoku.addAtIndexPosition(rowIndex, colIndex, possibilityWeights[0][1])
                squaresFilled = 1
                # print('Single weight found for rowIndex = ', rowIndex, ', colIndex ', colIndex, ', number is ', possibilityWeights[0][1])
            if possibilityWeights[0][0] > 1:
                mostCurrectNumber = 0
                mostSolvedSquares = 0
                for k in possibilityWeights:
                    copyOfSudokuGrid = sudoku.copyGrid()
                    copyOfSudoku = Sudoku(debugStr)
                    copyOfSudoku.assignGrid(copyOfSudokuGrid)
                    currentNumber = k[1]
                    copyOfSudoku.addAtIndexPosition(rowIndex, colIndex, currentNumber)
                    self.trySolvingForSudokuPuzzle(copyOfSudoku)
                    solvedSquares = copyOfSudoku.getCountOfSquaresFilled()
                    # print('Trying :  for rowIndex = ', rowIndex, ', colIndex ', colIndex, ', number is ', currentNumber, "solvedSquares", solvedSquares)
                    if solvedSquares == 81:
                        solvedGrid = copyOfSudoku.copyGrid()
                        sudoku.assignGrid(solvedGrid)
                        return squaresFilled
                    if solvedSquares > mostSolvedSquares:
                        mostSolvedSquares = solvedSquares
                        mostCurrectNumber = currentNumber
                    if mostCurrectNumber in allowedNumbers:
                        squaresFilled = 1
                        sudoku.addAtIndexPosition(rowIndex, colIndex, mostCurrectNumber)
                        # print('Multiple weight found for rowIndex = ', rowIndex, ', colIndex ', colIndex, ', most correct number is ', mostCurrectNumber, "mostSolvedSquares", mostSolvedSquares)
        return squaresFilled

    def fillNonUniqueNumbersForRow(self, sudoku, rowIndex, rowUnfilled):
        squaresFilled = 0
        for i in rowUnfilled:
            colIndex = i[1]
            squaresFilled += self.fillNonUniqueNumberForRowCol(sudoku, rowIndex, colIndex)
        return squaresFilled

    def fillNonUniqueNumbersForCol(self, sudoku, colIndex, colUnfilled):
        squaresFilled = 0
        for i in colUnfilled:
            rowIndex = i[0]
            squaresFilled += self.fillNonUniqueNumberForRowCol(sudoku, rowIndex, colIndex)
        return squaresFilled

    def fillUnknownNumbers(self, sudoku, maxLoops):
        loopAgain = True
        while (loopAgain):
            isSolved = sudoku.isSudokuSolved()
            if isSolved:
                # print("fillUnknownNumbers. Sudoku solved at maxLoop ", maxLoops)
                return
            #print("fillUnknownKnownNumbers, maxLoops left", maxLoops)
            maxLoops -= 1
            colsTried = []
            rowsTried = []
            for i in allowedColsRows:
                numberOfBoxesFilled = 0
                #print("In Row. Filled Squares =", numberOfBoxesFilled, ", Loop Count = ", i, self.sudoku)
                rowsWithMostFills = self.getMostFilledRowAndUnfilledIndices(sudoku, rowsTried)
                rowsTried.append(rowsWithMostFills[0])
                numberOfBoxesFilled += self.fillNonUniqueNumbersForRow(sudoku, rowsWithMostFills[0], rowsWithMostFills[1])

                #print("In Col. Filled Squares =", numberOfBoxesFilled, ", Loop Count = ", i, self.sudoku)
                colWithMostFills = self.getMostFilledColAndUnfilledIndices(sudoku, colsTried)
                colsTried.append(colWithMostFills[0])
                numberOfBoxesFilled += self.fillNonUniqueNumbersForCol(sudoku, colWithMostFills[0], colWithMostFills[1])
            if maxLoops == 0:
                loopAgain = False

    def trySolvingForSudokuPuzzle(self, sudoku):
        self.fillKnownNumbers(sudoku, 2)
        self.fillUnknownNumbers(sudoku, 2)
        return sudoku

def test1():
    # Test 1
    sudoku = Sudoku('Test 1')
    # Row 1
    sudoku.addAtPosition(1, 1, 8)
    sudoku.addAtPosition(1, 2, 3)
    sudoku.addAtPosition(1, 3, 5)
    sudoku.addAtPosition(1, 4, 7)
    sudoku.addAtPosition(1, 5, 4)
    # Row 2
    sudoku.addAtPosition(2, 5, 1)
    sudoku.addAtPosition(2, 6, 8)
    sudoku.addAtPosition(2, 7, 3)
    sudoku.addAtPosition(2, 8, 7)
    sudoku.addAtPosition(2, 9, 4)

    # Row 3
    sudoku.addAtPosition(3, 2, 4)
    sudoku.addAtPosition(3, 3, 7)
    sudoku.addAtPosition(3, 6, 6)
    sudoku.addAtPosition(3, 7, 8)
    sudoku.addAtPosition(3, 8, 5)

    # Row 4
    sudoku.addAtPosition(4, 2, 2)
    sudoku.addAtPosition(4, 4, 4)
    sudoku.addAtPosition(4, 5, 3)
    sudoku.addAtPosition(4, 6, 9)
    sudoku.addAtPosition(4, 8, 6)

    # Row5
    sudoku.addAtPosition(5, 2, 7)
    sudoku.addAtPosition(5, 3, 4)
    sudoku.addAtPosition(5, 4, 8)
    sudoku.addAtPosition(5, 8, 9)
    sudoku.addAtPosition(5, 9, 5)
    # Row 6
    sudoku.addAtPosition(6, 1, 9)
    sudoku.addAtPosition(6, 3, 1)
    sudoku.addAtPosition(6, 6, 5)
    sudoku.addAtPosition(6, 7, 4)
    sudoku.addAtPosition(6, 9, 8)

    # Row 7
    sudoku.addAtPosition(7, 1, 4)
    sudoku.addAtPosition(7, 4, 1)
    sudoku.addAtPosition(7, 6, 7)
    sudoku.addAtPosition(7, 7, 9)
    sudoku.addAtPosition(7, 9, 6)

    # Row 8
    sudoku.addAtPosition(8, 1, 7)
    sudoku.addAtPosition(8, 3, 6)
    sudoku.addAtPosition(8, 4, 9)
    sudoku.addAtPosition(8, 5, 2)
    sudoku.addAtPosition(8, 9, 3)

    # Row 9
    sudoku.addAtPosition(9, 1, 2)
    sudoku.addAtPosition(9, 2, 5)
    sudoku.addAtPosition(9, 6, 3)
    sudoku.addAtPosition(9, 7, 1)
    sudoku.addAtPosition(9, 8, 4)

    print(sudoku)
    solver = SudokuSolver()
    startTime = dt.datetime.utcnow()
    solver.fillUnknownNumbers(sudoku, 1)
    print(sudoku)
    endTime = dt.datetime.utcnow()
    print("Time taken", (endTime - startTime).microseconds, " microseconds")

def test2():
    # Test 2
    sudoku2 = Sudoku("Test 2")
    # Row 1
    sudoku2.addAtPosition(1, 1, 5)
    sudoku2.addAtPosition(1, 3, 9)
    sudoku2.addAtPosition(1, 5, 7)
    sudoku2.addAtPosition(1, 7, 3)

    # Row 2
    sudoku2.addAtPosition(2, 2, 7)
    sudoku2.addAtPosition(2, 3, 4)
    sudoku2.addAtPosition(2, 6, 8)
    sudoku2.addAtPosition(2, 8, 1)

    # Row 3
    sudoku2.addAtPosition(3, 6, 3)
    sudoku2.addAtPosition(3, 8, 7)
    sudoku2.addAtPosition(3, 9, 2)

    # Row 4
    sudoku2.addAtPosition(4, 2, 1)
    sudoku2.addAtPosition(4, 6, 6)
    sudoku2.addAtPosition(4, 8, 5)

    # Row 5
    sudoku2.addAtPosition(5, 1, 7)
    sudoku2.addAtPosition(5, 5, 4)
    sudoku2.addAtPosition(5, 6, 9)

    # Row 6
    sudoku2.addAtPosition(6, 2, 9)
    sudoku2.addAtPosition(6, 7, 7)
    sudoku2.addAtPosition(6, 8, 3)

    # Row 7
    sudoku2.addAtPosition(7, 3, 7)
    sudoku2.addAtPosition(7, 4, 8)
    sudoku2.addAtPosition(7, 9, 3)

    # Row 8
    sudoku2.addAtPosition(8, 1, 6)
    sudoku2.addAtPosition(8, 3, 2)
    sudoku2.addAtPosition(8, 4, 3)

    # Row 9
    sudoku2.addAtPosition(9, 2, 3)
    sudoku2.addAtPosition(9, 4, 4)
    sudoku2.addAtPosition(9, 7, 8)
    sudoku2.addAtPosition(9, 9, 6)
    print(sudoku2)

    solver = SudokuSolver()
    startTime = dt.datetime.utcnow()
    solver.fillUnknownNumbers(sudoku2, 3)
    print(sudoku2)
    endTime = dt.datetime.utcnow()
    print("Time taken", (endTime - startTime).microseconds, " microseconds")


def test3():
    # Test 3
    sudoku = Sudoku("Test 3")
    # Row 1
    sudoku.addAtPosition(1, 4, 8)
    sudoku.addAtPosition(1, 5, 4)
    sudoku.addAtPosition(1, 8, 7)

    # Row 2
    sudoku.addAtPosition(2, 3, 1)
    sudoku.addAtPosition(2, 5, 9)
    sudoku.addAtPosition(2, 7, 6)
    sudoku.addAtPosition(2, 9, 8)

    # Row 3
    sudoku.addAtPosition(3, 1, 5)
    sudoku.addAtPosition(3, 2, 2)

    # Row 4
    sudoku.addAtPosition(4, 5, 2)
    sudoku.addAtPosition(4, 6, 6)
    sudoku.addAtPosition(4, 7, 4)

    # Row 5
    sudoku.addAtPosition(5, 1, 9)
    sudoku.addAtPosition(5, 8, 5)

    # Row 6
    sudoku.addAtPosition(6, 2, 3)
    sudoku.addAtPosition(6, 4, 1)
    sudoku.addAtPosition(6, 9, 6)

    # Row 7
    sudoku.addAtPosition(7, 2, 1)
    sudoku.addAtPosition(7, 4, 3)
    sudoku.addAtPosition(7, 7, 5)

    # Row 8
    sudoku.addAtPosition(8, 6, 2)
    sudoku.addAtPosition(8, 7, 7)
    sudoku.addAtPosition(8, 8, 1)

    # Row 9
    sudoku.addAtPosition(9, 3, 4)
    print(sudoku)

    solver = SudokuSolver()
    startTime = dt.datetime.utcnow()
    # solver.fillKnownNumbers(sudoku, 3)
    # print("fillKnownNumbers 1 :", sudoku)
    solver.fillUnknownNumbers(sudoku, 3)
    print(sudoku)
    endTime = dt.datetime.utcnow()
    print("Time taken", (endTime - startTime).microseconds, " microseconds")


def main():
    test1()
    test2()
    test3()

if __name__ == "__main__":
    main()
