# O(n)
# n = len(dominoes)

from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        queue = deque()
        for i in range(len(dominoes)):
            if dominoes[i] != ".":
                queue.append(i)

        while len(queue) > 0:
            nextQueue = deque()
            pendingList = []
            while len(queue) > 0:
                i = queue.popleft()
                if dominoes[i] == "L":
                    self.fallLeft(dominoes, i, nextQueue, pendingList)
                elif dominoes[i] == "R":
                    self.fallRight(dominoes, i, nextQueue, pendingList)
            self.adjustPending(dominoes, pendingList)
            queue = nextQueue
        return "".join(dominoes)

    def adjustPending(self, dominoes, pendingList):
        for i in pendingList:
            if dominoes[i] == "LP":
                dominoes[i] = "L"
            elif dominoes[i] == "RP":
                dominoes[i] = "R"

    def fallLeft(self, dominoes, i, nextQueue, pendingList):
        if i > 0:
            if dominoes[i - 1] == ".":
                dominoes[i - 1] = "LP"
                pendingList.append(i - 1)
                nextQueue.append(i - 1)
            elif dominoes[i - 1] == "RP":
                dominoes[i - 1] = "."

    def fallRight(self, dominoes, i, nextQueue, pendingList):
        if i < len(dominoes) - 1:
            if dominoes[i + 1] == ".":
                dominoes[i + 1] = "RP"
                pendingList.append(i + 1)
                nextQueue.append(i + 1)
            elif dominoes[i + 1] == "LP":
                dominoes[i + 1] = "."
