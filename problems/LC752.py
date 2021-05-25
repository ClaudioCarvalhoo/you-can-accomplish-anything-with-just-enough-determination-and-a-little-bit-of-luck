# O(1)
# max combinations is 10000

from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if target in deadends or "0000" in deadends:
            return -1

        visited = set()
        queue = deque()
        queue.append(("0000", 0))
        while len(queue) > 0:
            state, moves = queue.popleft()
            if state == target:
                return moves
            candidates = self.generateMoves(state, deadends, visited)
            for candidate in candidates:
                queue.append((candidate, moves + 1))
        return -1

    def generateMoves(self, state, deadends, visited):
        res = []
        for i in range(4):
            for j in [-1, 1]:
                candidate = state[:i] + str((int(state[i]) + j) % 10) + state[i + 1 :]
                if candidate not in deadends and candidate not in visited:
                    res.append(candidate)
                    visited.add(candidate)
        return res
