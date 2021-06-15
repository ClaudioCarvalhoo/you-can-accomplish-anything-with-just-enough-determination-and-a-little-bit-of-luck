# O(1)


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        xWins = self.isWinner(board, "X")
        oWins = self.isWinner(board, "O")
        winner = None
        if xWins and oWins:
            return False
        elif xWins:
            winner = "X"
        elif oWins:
            winner = "O"
        return self.validateQuantity(board, winner)

    def isWinner(self, board, player):
        for y in range(3):
            if board[y][0] == board[y][1] == board[y][2] == player:
                return True
        for x in range(3):
            if board[0][x] == board[1][x] == board[2][x] == player:
                return True
        if board[1][1] == player:
            if (
                board[0][0] == board[1][1] == board[2][2]
                or board[0][2] == board[1][1] == board[2][0]
            ):
                return True
        return False

    def validateQuantity(self, board, winner):
        xQuant = 0
        oQuant = 0
        for y in range(3):
            for x in range(3):
                if board[y][x] == "X":
                    xQuant += 1
                elif board[y][x] == "O":
                    oQuant += 1
        if winner == "X":
            return xQuant == oQuant + 1
        elif winner == "O":
            return xQuant == oQuant
        else:
            return xQuant == oQuant + 1 or xQuant == oQuant
