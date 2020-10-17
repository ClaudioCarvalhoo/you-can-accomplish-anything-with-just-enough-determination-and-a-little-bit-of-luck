# O(n * m * min(n, m))
# n = len(grid)
# m = len(grid[x])


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rights = {}
        downs = {}

        res = 0

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    if not (y, x) in rights:
                        self.howManyToTheRight(grid, y, x, rights)
                    if not (y, x) in downs:
                        self.howManyDownwards(grid, y, x, downs)

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    side = min(rights[(y, x)], downs[(y, x)])
                    while int(math.pow(side + 1, 2)) > res:
                        if (
                            rights[(y + side, x)] >= side
                            and downs[(y, x + side)] >= side
                        ):
                            res = int(math.pow(side + 1, 2))
                            break
                        else:
                            side -= 1

        return res

    def howManyToTheRight(self, grid, y, x, rights):
        if x >= len(grid[y]) - 1 or grid[y][x + 1] == 0:
            rights[(y, x)] = 0
            return 0
        else:
            rights[(y, x)] = self.howManyToTheRight(grid, y, x + 1, rights) + 1
            return rights[(y, x)]

    def howManyDownwards(self, grid, y, x, downs):
        if y >= len(grid) - 1 or grid[y + 1][x] == 0:
            downs[(y, x)] = 0
            return 0
        else:
            downs[(y, x)] = self.howManyDownwards(grid, y + 1, x, downs) + 1
            return downs[(y, x)]