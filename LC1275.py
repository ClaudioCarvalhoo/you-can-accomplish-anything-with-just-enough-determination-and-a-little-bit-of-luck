# O(1)


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) < 5:
            return "Pending"

        grid = [[None for _ in range(3)] for _ in range(3)]
        isA = True
        for move in moves:
            grid[move[1]][move[0]] = isA
            isA = not isA

        horizontalWinner = self.checkHorizontals(grid)
        if horizontalWinner[0]:
            return self.returnWinner(horizontalWinner[1])

        verticalWinner = self.checkVerticals(grid)
        if verticalWinner[0]:
            return self.returnWinner(verticalWinner[1])

        diagonalWinner = self.checkDiagonals(grid)
        if diagonalWinner[0]:
            return self.returnWinner(diagonalWinner[1])

        if len(moves) < 9:
            return "Pending"
        else:
            return "Draw"

    def checkHorizontals(self, grid):
        for x in range(3):
            if grid[0][x] is not None and grid[0][x] == grid[1][x] == grid[2][x]:
                return (True, grid[0][x])
        return (False, None)

    def checkVerticals(self, grid):
        for y in range(3):
            if grid[y][0] is not None and grid[y][0] == grid[y][1] == grid[y][2]:
                return (True, grid[y][0])
        return (False, None)

    def checkDiagonals(self, grid):
        if grid[1][1] is not None and (
            grid[0][0] == grid[1][1] == grid[2][2]
            or grid[2][0] == grid[1][1] == grid[0][2]
        ):
            return (True, grid[1][1])
        return (False, None)

    def returnWinner(self, isWinnerA):
        return "A" if isWinnerA else "B"