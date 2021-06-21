# O(1) - But better than brute-force due to backtracking


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        quadrants = [set() for _ in range(9)]
        self.populateWithInitialValues(board, rows, columns, quadrants)

        self.solve(board, 0, 0, rows, columns, quadrants)

    def solve(self, board, y, x, rows, columns, quadrants):
        if y >= 9:
            return True
        nextY = y + 1 if x == 8 else y
        nextX = x + 1 if x < 8 else 0
        if board[y][x] != ".":
            return self.solve(board, nextY, nextX, rows, columns, quadrants)
        else:
            for num in range(1, 10):
                num = str(num)
                if (
                    num not in rows[y]
                    and num not in columns[x]
                    and num not in quadrants[self.findQuadrant(y, x)]
                ):
                    rows[y].add(num)
                    columns[x].add(num)
                    quadrants[self.findQuadrant(y, x)].add(num)
                    board[y][x] = num
                    if self.solve(board, nextY, nextX, rows, columns, quadrants):
                        return True
                    rows[y].remove(num)
                    columns[x].remove(num)
                    quadrants[self.findQuadrant(y, x)].remove(num)
                    board[y][x] = "."
            return False

    def populateWithInitialValues(self, board, rows, columns, quadrants):
        for y in range(9):
            for x in range(9):
                if board[y][x] != ".":
                    num = board[y][x]
                    rows[y].add(num)
                    columns[x].add(num)
                    quadrants[self.findQuadrant(y, x)].add(num)

    def findQuadrant(self, y, x):
        quadrant = 3 * (y // 3)
        quadrant += x // 3
        return quadrant