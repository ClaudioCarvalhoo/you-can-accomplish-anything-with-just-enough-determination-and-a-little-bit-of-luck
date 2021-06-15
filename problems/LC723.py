# O((n*m)²)
# n = len(board) | m = len(board[0])


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        didCrush = True
        while didCrush:
            didCrush = self.crush(board)
            self.gravity(board)
        return board

    def crush(self, board):
        didCrush = False
        for y in range(len(board)):
            self.markRow(board, y)
        for x in range(len(board[0])):
            self.markColumn(board, x)
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] < 0:
                    board[y][x] = 0
                    didCrush = True
        return didCrush

    def markRow(self, board, y):
        start = 0
        end = 0
        while end < len(board[y]):
            while end + 1 < len(board[y]) and abs(board[y][end + 1]) == abs(
                board[y][start]
            ):
                end += 1
            if end - start >= 2:
                for x in range(start, end + 1):
                    board[y][x] = -1 * abs(board[y][x])
            start = end + 1
            end = start

    def markColumn(self, board, x):
        start = 0
        end = 0
        while end < len(board):
            while end + 1 < len(board) and abs(board[end + 1][x]) == abs(
                board[start][x]
            ):
                end += 1
            if end - start >= 2:
                for y in range(start, end + 1):
                    board[y][x] = -1 * abs(board[y][x])
            start = end + 1
            end = start

    def gravity(self, board):
        for x in range(len(board[0])):
            nextCandyY = len(board) - 1
            for y in range(len(board) - 1, -1, -1):
                while nextCandyY >= 0 and board[nextCandyY][x] == 0:
                    nextCandyY -= 1
                if nextCandyY < 0:
                    board[y][x] = 0
                else:
                    board[y][x] = board[nextCandyY][x]
                    nextCandyY -= 1