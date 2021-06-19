# O(n*m)
# n = len(matrix) | m = len(matrix[0])


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        increasingPathSize = [[None for _ in row] for row in matrix]
        res = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                res = max(
                    res, self.calcIncreasingPathSize(matrix, y, x, increasingPathSize)
                )
        return res

    def calcIncreasingPathSize(self, matrix, y, x, increasingPathSize):
        if increasingPathSize[y][x] is not None:
            return increasingPathSize[y][x]
        increasingPathSize[y][x] = 1
        for neighborY, neighborX in self.getNeighbors(matrix, y, x):
            if matrix[neighborY][neighborX] > matrix[y][x]:
                increasingPathSize[y][x] = max(
                    increasingPathSize[y][x],
                    1
                    + self.calcIncreasingPathSize(
                        matrix, neighborY, neighborX, increasingPathSize
                    ),
                )
        return increasingPathSize[y][x]

    def getNeighbors(self, matrix, y, x):
        neighbors = []
        if y > 0:
            neighbors.append((y - 1, x))
        if y < len(matrix) - 1:
            neighbors.append((y + 1, x))
        if x > 0:
            neighbors.append((y, x - 1))
        if x < len(matrix[y]) - 1:
            neighbors.append((y, x + 1))
        return neighbors