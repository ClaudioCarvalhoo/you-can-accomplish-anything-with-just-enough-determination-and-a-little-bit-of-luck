# Sol 1
class Leaderboard:
    # O(1)
    def __init__(self):
        self.leaderboardHead = Node(None)
        self.positions = {}

    # O(n)
    def addScore(self, playerId: int, score: int) -> None:
        newNode = Node(score)
        if playerId in self.positions:
            newNode.val += self.positions[playerId].val
            self.reset(playerId)
        self.positions[playerId] = newNode
        previous = self.leaderboardHead
        while previous.next is not None and previous.next.val > newNode.val:
            previous = previous.next
        newNode.prev = previous
        newNode.next = previous.next
        if previous.next is not None:
            previous.next.prev = newNode
        previous.next = newNode

    # O(k)
    def top(self, K: int) -> int:
        res = 0
        node = self.leaderboardHead.next
        for _ in range(K):
            res += node.val
            node = node.next
            if node is None:
                break
        return res

    # O(1)
    def reset(self, playerId: int) -> None:
        playerNode = self.positions[playerId]
        playerNode.prev.next = playerNode.next
        if playerNode.next is not None:
            playerNode.next.prev = playerNode.prev
        del self.positions[playerId]


class Node:
    def __init__(self, val, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev


# Sol 2
import heapq


class Leaderboard:

    # O(1)
    def __init__(self):
        self.scores = {}

    # O(1)
    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scores:
            self.scores[playerId] += score
        else:
            self.scores[playerId] = score

    # O(n*log(k))
    def top(self, K: int) -> int:
        heap = []
        for playerId in self.scores:
            heapq.heappush(heap, self.scores[playerId])
            if len(heap) > K:
                heapq.heappop(heap)
        res = 0
        for score in heap:
            res += score
        return res

    # O(1)
    def reset(self, playerId: int) -> None:
        del self.scores[playerId]