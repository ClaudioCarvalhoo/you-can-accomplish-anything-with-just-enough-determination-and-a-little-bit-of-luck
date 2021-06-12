# O(n*m)
# n = len(obstaclesGrid) | m = len(obstaclesGrid[0])


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        waysToGetTo = [[None for _ in obstacleGrid[0]] for _ in obstacleGrid]
        waysToGetTo[0][0] = 1
        return self.calcPaths(
            obstacleGrid, waysToGetTo, len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1
        )

    def calcPaths(self, obstacleGrid, waysToGetTo, y, x):
        if x < 0 or y < 0 or obstacleGrid[y][x] == 1:
            return 0
        if waysToGetTo[y][x] != None:
            return waysToGetTo[y][x]
        waysToGetTo[y][x] = self.calcPaths(
            obstacleGrid, waysToGetTo, y - 1, x
        ) + self.calcPaths(obstacleGrid, waysToGetTo, y, x - 1)
        return waysToGetTo[y][x]