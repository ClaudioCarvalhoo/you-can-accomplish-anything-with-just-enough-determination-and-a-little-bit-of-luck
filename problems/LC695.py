# O(n*m)
# n = len(grid) | m = len(grid[0])


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    maxArea = max(maxArea, self.explore(grid, y, x))
        return maxArea

    def explore(self, grid, y, x):
        res = 1
        grid[y][x] = 0
        for neighbor in self.getNeighbors(grid, y, x):
            neighborY, neighborX = neighbor
            if grid[neighborY][neighborX] == 1:
                res += self.explore(grid, neighborY, neighborX)
        return res

    def getNeighbors(self, grid, y, x):
        res = []
        if y - 1 >= 0:
            res.append((y - 1, x))
        if y + 1 < len(grid):
            res.append((y + 1, x))
        if x - 1 >= 0:
            res.append((y, x - 1))
        if x + 1 < len(grid[y]):
            res.append((y, x + 1))
        return res