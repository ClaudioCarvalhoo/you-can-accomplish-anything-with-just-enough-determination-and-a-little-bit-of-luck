# O(n*m)
# n=len(matrix) | m=len(matrix[0])

from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        pacific = {}
        atlantic = {}
        for i in range(len(matrix[0])):
            self.explore(matrix, 0, i, pacific)
        for i in range(len(matrix)):
            self.explore(matrix, i, 0, pacific)
        for i in range(len(matrix[-1])):
            self.explore(matrix, len(matrix) - 1, i, atlantic)
        for i in range(len(matrix)):
            self.explore(matrix, i, len(matrix[i]) - 1, atlantic)
        res = []
        for key in pacific:
            if key in atlantic:
                res.append([key[0], key[1]])
        return res

    def explore(self, matrix, y, x, ocean):
        if (y, x) in ocean:
            return
        else:
            ocean[(y, x)] = True
            currentElevation = matrix[y][x]
            if y - 1 >= 0 and matrix[y - 1][x] >= currentElevation:
                self.explore(matrix, y - 1, x, ocean)
            if x + 1 < len(matrix[y]) and matrix[y][x + 1] >= currentElevation:
                self.explore(matrix, y, x + 1, ocean)
            if y + 1 < len(matrix) and matrix[y + 1][x] >= currentElevation:
                self.explore(matrix, y + 1, x, ocean)
            if x - 1 >= 0 and matrix[y][x - 1] >= currentElevation:
                self.explore(matrix, y, x - 1, ocean)
