newline = '\n'
allowedNumbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
allowedColsRows = (0, 1, 2, 3, 4, 5, 6, 7, 8)
homeSquareRowColIndex = (1, 4, 7)


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
            grid[i].append(0)
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

    def addAtIndexPosition(self, rowIndex, colIndex, value):
        self.addAtPosition(rowIndex + 1, colIndex + 1, value)
        return self

    # User input. Reduce 1 to get actual index for row and column
    def addAtPosition(self, rowNum, colNum, value):
        rowIndex = rowNum - 1
        colIndex = colNum - 1
        valueToChange = value
        if not rowIndex in allowedColsRows:
            return
        if not colIndex in allowedColsRows:
            return
        if not valueToChange in allowedNumbers:
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


class SudokuSolver:
    def __init__(self, sudokuPuzzle):
        self.sudoku = sudokuPuzzle

    def __repr__(self):
        return self.sudoku.__repr__()

    def getMostFilledRowAndUnfilledIndices(self, skipList):
        rowMax = 0
        rowIndex = 0
        rowIndices = []
        for i in allowedColsRows:
            if not i in skipList:
                filledRows = self.sudoku.getNumbersInRow(i)
                if len(filledRows) > rowMax:
                    rowMax = len(filledRows)
                    rowIndex = i
                    rowIndices = self.sudoku.getUnfilledIndicesInRow(i)
        return [rowIndex, rowIndices]

    def getMostFilledColAndUnfilledIndices(self, skipList):
        colMax = 0
        colIndex = 0
        colIndices = []
        for i in allowedColsRows:
            if not i in skipList:
                filledCols = self.sudoku.getNumbersInCol(i)
                if len(filledCols) > colMax:
                    colMax = len(filledCols)
                    colIndex = i
                    colIndices = self.sudoku.getUnfilledIndicesInCol(i)
        return [colIndex, colIndices]

    def fillUniqueNumberForRowCol(self, rowIndex, colIndex):
        squaresFilled = 0
        possibleNumbersInRow = self.sudoku.getPossibleNumbersInRow(rowIndex)
        possibleNumbersInCol = self.sudoku.getPossibleNumbersInCol(colIndex)
        possibleNumbersInHomeSquare = self.sudoku.getPossibleNumbersInHomeSquare(rowIndex, colIndex)
        print("fillUniqueNumberForRowCol. RowIndex =", rowIndex, ", ColIndex =", colIndex, ", possibleNumbersInRow = ",
              possibleNumbersInRow, ", possibleNumbersInCol = ", possibleNumbersInCol,
              " possibleNumbersInHomeSquare = ", possibleNumbersInHomeSquare)
        rowColPossibilities = tuple(set(possibleNumbersInRow).intersection(possibleNumbersInCol))
        rowColSquarePossibilities = tuple(set(rowColPossibilities).intersection(possibleNumbersInHomeSquare))
        print("fillUniqueNumberForRowCol. RowIndex =", rowIndex, ", ColIndex =", colIndex,
              ", rowColSquarePossibilities = ", rowColSquarePossibilities)
        if len(rowColSquarePossibilities) == 1:
            print('Unique Match found for rowIndex = ', rowIndex, ', colIndex ', colIndex, ', number is ',
                  list(rowColSquarePossibilities)[0])
            self.sudoku.addAtIndexPosition(rowIndex, colIndex, list(rowColSquarePossibilities)[0])
            squaresFilled = 1
        else:
            print('Non-Unique Match found for rowIndex = ', rowIndex, ', colIndex ', colIndex, ', number is ',
                  list(rowColSquarePossibilities))
        return squaresFilled

    def fillUniqueNumbersForRow(self, rowIndex, rowUnfilled):
        squaresFilled = 0
        for i in rowUnfilled:
            colIndex = i[1]
            squaresFilled += self.fillUniqueNumberForRowCol(rowIndex, colIndex)
        return squaresFilled

    def fillUniqueNumbersForCol(self, colIndex, colUnfilled):
        squaresFilled = 0
        for i in colUnfilled:
            rowIndex = i[0]
            squaresFilled += self.fillUniqueNumberForRowCol(rowIndex, colIndex)
        return squaresFilled

    def fillKnownNumbers(self, maxLoops):
        numberOfBoxesFilled = 0
        loopAgain = True
        while (loopAgain):
            maxLoops -= 1
            colsTried = []
            rowsTried = []
            for i in allowedColsRows:
                print("In Row. Filled Squares =", numberOfBoxesFilled, ", Loop Count = ", i, self.sudoku)
                rowsWithMostFills = self.getMostFilledRowAndUnfilledIndices(rowsTried)
                rowsTried.append(rowsWithMostFills[0])
                numberOfBoxesFilled += self.fillUniqueNumbersForRow(rowsWithMostFills[0], rowsWithMostFills[1])

                print("In Col. Filled Squares =", numberOfBoxesFilled, ", Loop Count = ", i, self.sudoku)
                colWithMostFills = self.getMostFilledColAndUnfilledIndices(colsTried)
                colsTried.append(colWithMostFills[0])
                numberOfBoxesFilled += self.fillUniqueNumbersForCol(colWithMostFills[0], colWithMostFills[1])
            if numberOfBoxesFilled > 0 | maxLoops > 0:
                loopAgain = True


def main():
    sudoku = Sudoku('Test 1')
    # Row 1
    sudoku.addAtPosition(1, 1, 8)
    sudoku.addAtPosition(1, 2, 3)
    sudoku.addAtPosition(1, 3, 5)
    sudoku.addAtPosition(1, 4, 7)
    sudoku.addAtPosition(1, 5, 5)
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
    sudoku.addAtPosition(4, 4, 3)
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

    # numbersInRow = sudoku.getNumbersInRow(0)
    # print(numbersInRow)

    # numbersInCol = sudoku.getNumbersInCol(2)
    #print(numbersInCol)

    # print(sudoku.getNumbersInHomeSquare(0, 0))
    # print(sudoku.getUnfilledRowColIndicesInHomeSquare(1, 1))
    # print(sudoku.getUnfilledIndicesInRow(8))
    # print(sudoku.getUnfilledIndicesInCol(2))

    solver = SudokuSolver(sudoku)
    print("Most filed col", solver.getMostFilledColAndUnfilledIndices([]))
    print("Most filled row", solver.getMostFilledRowAndUnfilledIndices([]))

    solver.fillKnownNumbers(1)


if __name__ == "__main__":
    main()
