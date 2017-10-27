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
        return

    def getNumbersInRow(self, rowIndex):
        rowInQuestion = self.grid[rowIndex]
        retVal = []
        for i in rowInQuestion:
            if i in allowedNumbers:
                retVal.append(i)
        return retVal

    def getNumbersInCol(self, colIndex):
        retVal = []
        for i in allowedColsRows:
            rowInQuestion = self.grid[i]
            if rowInQuestion[colIndex] in allowedNumbers:
                retVal.append(rowInQuestion[colIndex])
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

    def getUnfilledRowColIndicesInHomeSquare(self, rowIndex, colIndex):
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


def main():
    sudoku = Sudoku('Test')
    sudoku.addAtPosition(1, 1, 1)
    sudoku.addAtPosition(2, 2, 2)
    sudoku.addAtPosition(2, 3, 4)
    sudoku.addAtPosition(3, 3, 3)
    sudoku.addAtPosition(4, 4, 4)
    sudoku.addAtPosition(5, 5, 5)
    sudoku.addAtPosition(6, 6, 6)
    sudoku.addAtPosition(7, 7, 7)
    sudoku.addAtPosition(8, 8, 8)
    sudoku.addAtPosition(9, 9, 9)
    sudoku.addAtPosition(9, 9, 10)
    sudoku.addAtPosition(10, 10, 9)
    print(sudoku)

    numbersInRow = sudoku.getNumbersInRow(0)
    print(numbersInRow)

    numbersInCol = sudoku.getNumbersInCol(2)
    print(numbersInCol)

    print(sudoku.getNumbersInHomeSquare(0, 0))


if __name__ == "__main__":
    main()
