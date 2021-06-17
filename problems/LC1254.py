# O(n*m)
# n = len(grid) | m = len(grid[0])


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 0 and self.explore(grid, y, x):
                    ans += 1
        return ans

    def explore(self, grid, y, x):
        if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
            return False
        if grid[y][x] == 1:
            return True
        grid[y][x] = 1
        isClosed = True
        for neighborY, neighborX in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
            isClosed = self.explore(grid, neighborY, neighborX) and isClosed
        return isClosed