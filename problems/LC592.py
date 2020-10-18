# O(n²)
# n = len(board)


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.reveal(board, click[0], click[1])
        return board

    def isUnrevealed(self, board, y, x):
        if board[y][x] == "M" or board[y][x] == "E":
            return True
        else:
            return False

    def getMinesNearby(self, board, y, x):
        total = 0
        if y - 1 >= 0 and board[y - 1][x] == "M":
            total += 1
        if y - 1 >= 0 and x - 1 >= 0 and board[y - 1][x - 1] == "M":
            total += 1
        if y - 1 >= 0 and x + 1 < len(board[y]) and board[y - 1][x + 1] == "M":
            total += 1
        if x - 1 >= 0 and board[y][x - 1] == "M":
            total += 1
        if x + 1 < len(board[y]) and board[y][x + 1] == "M":
            total += 1
        if y + 1 < len(board) and board[y + 1][x] == "M":
            total += 1
        if y + 1 < len(board) and x + 1 < len(board[y]) and board[y + 1][x + 1] == "M":
            total += 1
        if y + 1 < len(board) and x - 1 >= 0 and board[y + 1][x - 1] == "M":
            total += 1
        return total

    def reveal(self, board, y, x):
        if (
            y < 0
            or y >= len(board)
            or x < 0
            or x >= len(board[y])
            or not self.isUnrevealed(board, y, x)
        ):
            return

        if board[y][x] == "M":
            board[y][x] = "X"
        else:
            minesNearby = self.getMinesNearby(board, y, x)
            if minesNearby == 0:
                board[y][x] = "B"
                self.reveal(board, y - 1, x)
                self.reveal(board, y - 1, x - 1)
                self.reveal(board, y - 1, x + 1)
                self.reveal(board, y, x + 1)
                self.reveal(board, y, x - 1)
                self.reveal(board, y + 1, x)
                self.reveal(board, y + 1, x - 1)
                self.reveal(board, y + 1, x + 1)
            else:
                board[y][x] = str(minesNearby)