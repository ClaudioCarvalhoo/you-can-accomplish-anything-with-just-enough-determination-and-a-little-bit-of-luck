# O(n*m*min(n, m))
# n = len(grid) | m = len(grid[0])


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rowSum = self.buildRowSum(grid)
        columnSum = self.buildColumnSum(grid)
        firstDiagonalSum = self.buildFirstDiagonalSum(grid)
        secondDiagonalSum = self.buildSecondDiagonalSum(grid)

        height = len(grid)
        width = len(grid[0])
        maxSquareSize = min(height, width)

        for size in range(maxSquareSize, 1, -1):
            for y in range(len(grid) - size + 1):
                for x in range(len(grid[y]) - size + 1):
                    if self.isMagicSquare(
                        grid,
                        y,
                        x,
                        size,
                        rowSum,
                        columnSum,
                        firstDiagonalSum,
                        secondDiagonalSum,
                    ):
                        return size
        return 1

    def buildRowSum(self, grid):
        rowSum = []
        for y in range(len(grid)):
            rowSum.append([])
            runningSum = 0
            for x in range(len(grid[y])):
                runningSum += grid[y][x]
                rowSum[-1].append(runningSum)
        return rowSum

    def buildColumnSum(self, grid):
        columnSum = []
        for x in range(len(grid[0])):
            columnSum.append([])
            runningSum = 0
            for y in range(len(grid)):
                runningSum += grid[y][x]
                columnSum[-1].append(runningSum)
        return columnSum

    def buildFirstDiagonalSum(self, grid):
        firstDiagonalSum = []
        for y in range(len(grid)):
            firstDiagonalSum.append([])
            for x in range(len(grid[y])):
                prev = 0
                if y > 0 and x > 0:
                    prev = firstDiagonalSum[y - 1][x - 1]
                firstDiagonalSum[-1].append(prev + grid[y][x])
        return firstDiagonalSum

    def buildSecondDiagonalSum(self, grid):
        secondDiagonalSum = []
        for y in range(len(grid)):
            secondDiagonalSum.append([])
            for x in range(len(grid[y])):
                prev = 0
                if y > 0 and x < len(grid[y]) - 1:
                    prev = secondDiagonalSum[y - 1][x + 1]
                secondDiagonalSum[-1].append(prev + grid[y][x])
        return secondDiagonalSum

    def isMagicSquare(
        self, grid, y, x, size, rowSum, columnSum, firstDiagonalSum, secondDiagonalSum
    ):
        target = firstDiagonalSum[y + size - 1][x + size - 1]
        if y > 0 and x > 0:
            target -= firstDiagonalSum[y - 1][x - 1]
        secondDiagonal = secondDiagonalSum[y + size - 1][x]
        if y > 0 and x + size - 1 < len(grid[y]) - 1:
            secondDiagonal -= secondDiagonalSum[y - 1][x + size]
        if secondDiagonal != target:
            return False
        for offset in range(size):
            row = rowSum[y + offset][x + size - 1]
            if x > 0:
                row -= rowSum[y + offset][x - 1]
            if row != target:
                return False
            column = columnSum[x + offset][y + size - 1]
            if y > 0:
                column -= columnSum[x + offset][y - 1]
            if column != target:
                return False
        return True
