# O(n*m)
# n = len(grid) | m = len(grid[0])


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        twoStartY, twoStartX = None, None
        for y in range(len(grid) - 1, -1, -1):
            for x in range(len(grid[y]) - 1, -1, -1):
                if grid[y][x] == 1:
                    self.markIslandAsTwo(grid, y, x)
                    twoStartY, twoStartX = y, x
                    break
            if twoStartY is not None:
                break

        shortestPathToTwo = [[float("inf") for _ in grid[y]] for y in range(len(grid))]
        self.calculateShortestPathsToTwo(grid, shortestPathToTwo, twoStartY, twoStartX)

        return self.findClosestOneToTwo(grid, shortestPathToTwo)

    def markIslandAsTwo(self, grid, y, x):
        grid[y][x] = 2
        neighbors = self.getNeighbors(grid, y, x)
        for neighborY, neighborX in neighbors:
            if grid[neighborY][neighborX] == 1:
                self.markIslandAsTwo(grid, neighborY, neighborX)

    def calculateShortestPathsToTwo(
        self, grid, shortestPathToTwo, twoStartY, twoStartX
    ):
        allTwos = []
        self.findAllTwos(grid, twoStartY, twoStartX, allTwos, set())
        toVisit = allTwos
        seen = set(allTwos)
        distance = 0
        while len(toVisit) > 0:
            visitNext = []
            for y, x in toVisit:
                shortestPathToTwo[y][x] = distance
                neighbors = self.getNeighbors(grid, y, x)
                for neighbor in neighbors:
                    if neighbor not in seen:
                        visitNext.append(neighbor)
                        seen.add(neighbor)
            distance += 1
            toVisit = visitNext

    def findAllTwos(self, grid, y, x, res, visited):
        res.append((y, x))
        visited.add((y, x))
        neighbors = self.getNeighbors(grid, y, x)
        for neighborY, neighborX in neighbors:
            if (neighborY, neighborX) not in visited and grid[neighborY][
                neighborX
            ] == 2:
                self.findAllTwos(grid, neighborY, neighborX, res, visited)

    def findClosestOneToTwo(self, grid, shortestPathToTwo):
        res = float("inf")
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    res = min(res, shortestPathToTwo[y][x])
        return res - 1

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