class NumMatrix:

    # O(n*m)
    def __init__(self, matrix: List[List[int]]):
        self.sumFromOrigin = [[0 for _ in row] for row in matrix]
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                self.sumFromOrigin[y][x] = matrix[y][x]
                if y - 1 >= 0:
                    self.sumFromOrigin[y][x] += self.sumFromOrigin[y - 1][x]
                if x - 1 >= 0:
                    self.sumFromOrigin[y][x] += self.sumFromOrigin[y][x - 1]
                if x - 1 >= 0 and y - 1 >= 0:
                    self.sumFromOrigin[y][x] -= self.sumFromOrigin[y - 1][x - 1]

    # O(1)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        regionSum = self.sumFromOrigin[row2][col2]
        if row1 - 1 >= 0:
            regionSum -= self.sumFromOrigin[row1 - 1][col2]
        if col1 - 1 >= 0:
            regionSum -= self.sumFromOrigin[row2][col1 - 1]
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            regionSum += self.sumFromOrigin[row1 - 1][col1 - 1]
        return regionSum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)