# O(n*log(k))
# n = len(words) | k = k


import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = {}
        for word in words:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1

        heap = []
        for word in counter.keys():
            heapq.heappush(heap, Word(word, counter[word]))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        res.reverse()
        return res


class Word:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        else:
            return self.count < other.count