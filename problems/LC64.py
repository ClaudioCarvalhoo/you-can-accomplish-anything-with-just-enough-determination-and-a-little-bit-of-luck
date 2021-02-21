# O(n*m)
# n = len(grid) | m = len(grid[0])

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        distances = [[None for _ in grid[0]] for _ in grid]
        distances[0][0] = grid[0][0]

        offset = 0
        while distances[-1][-1] == None:
            for i in range(max(1, offset), len(grid)):
                distances[i][offset] = (
                    min(
                        self.getDistance(distances, i - 1, offset),
                        self.getDistance(distances, i, offset - 1),
                    )
                    + grid[i][offset]
                )
            for i in range(max(1, offset), len(grid[0])):
                distances[offset][i] = (
                    min(
                        self.getDistance(distances, offset - 1, i),
                        self.getDistance(distances, offset, i - 1),
                    )
                    + grid[offset][i]
                )
            offset += 1
        return distances[-1][-1]

    def getDistance(self, distances, y, x):
        if x < 0 or y < 0:
            return float("inf")
        else:
            return distances[y][x]