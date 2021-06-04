# O(n) - Considering only 26 possible letters in heap
# n = len(S)

from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        charCount = Counter(S)
        heap = [(-charCount[char], char) for char in charCount]
        heapq.heapify(heap)

        res = []
        onHold = None
        for i in range(len(S)):
            if len(heap) == 0:
                return ""
            count, char = heapq.heappop(heap)
            res.append(char)
            if onHold is not None:
                heapq.heappush(heap, onHold)
            if count + 1 != 0:
                onHold = (count + 1, char)
            else:
                onHold = None
        return "".join(res)
