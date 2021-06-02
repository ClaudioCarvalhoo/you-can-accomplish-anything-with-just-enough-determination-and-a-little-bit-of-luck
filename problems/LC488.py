from collections import Counter, deque


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        board = [ball for ball in board]
        handDict = {"R": 0, "Y": 0, "B": 0, "G": 0, "W": 0}
        for ball in hand:
            handDict[ball] += 1

        queue = deque([(board, handDict, 0)])
        visited = set()
        while len(queue) > 0:
            board, hand, plays = queue.popleft()
            newBoard = self.popMatches(board)
            stateHash = self.hashState(newBoard, hand)
            if stateHash in visited:
                continue
            if len(newBoard) == 0:
                return plays
            for ball in hand:
                if hand[ball] > 0:
                    for i in range(len(newBoard)):
                        if i + 1 == len(newBoard) or newBoard[i + 1] != ball:
                            newHand = hand.copy()
                            newHand[ball] -= 1
                            queue.append(
                                (
                                    newBoard[:i] + [ball] + newBoard[i:],
                                    newHand,
                                    plays + 1,
                                )
                            )
            visited.add(stateHash)
        return -1

    def popMatches(self, board):
        newBoard = []
        i = 0
        while i < len(board):
            ball = board[i]
            count = 1
            toAdd = 1
            toPop = 0
            j = len(newBoard) - 1
            while j >= 0 and newBoard[j] == ball:
                count += 1
                toPop += 1
                j -= 1
            while i + 1 < len(board) and board[i + 1] == ball:
                count += 1
                toAdd += 1
                i += 1
            if count < 3:
                newBoard += [ball] * toAdd
            else:
                for _ in range(toPop):
                    newBoard.pop()
            i += 1
        return newBoard

    def hashState(self, board, hand):
        return ("".join(board), hand["R"], hand["Y"], hand["B"], hand["G"], hand["W"])
