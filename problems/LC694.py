# O(n*m)
# n = len(grid) | m = len(grid[0])


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        res = 0
        islands = set()
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    path = []
                    self.explore(grid, y, x, 0, 0, path)
                    islands.add(tuple(path))
        return len(islands)

    def explore(self, grid, y, x, relativeY, relativeX, path):
        if grid[y][x] == 1:
            path.append((relativeY, relativeX))
            grid[y][x] = 0
            neighbors = self.getNeighbors(grid, y, x, relativeY, relativeX)
            for neighbor in neighbors:
                self.explore(
                    grid, neighbor[0], neighbor[1], neighbor[2], neighbor[3], path
                )

    def getNeighbors(self, grid, y, x, relativeY, relativeX):
        neighbors = []
        if x > 0:
            neighbors.append((y, x - 1, relativeY, relativeX - 1))
        if x < len(grid[y]) - 1:
            neighbors.append((y, x + 1, relativeY, relativeX + 1))
        if y > 0:
            neighbors.append((y - 1, x, relativeY - 1, relativeX))
        if y < len(grid) - 1:
            neighbors.append((y + 1, x, relativeY + 1, relativeX))
        return neighbors