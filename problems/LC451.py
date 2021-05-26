# O(n)
# n = len(s)

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        maxCount = max(counter.values())

        buckets = [[] for _ in range(maxCount)]
        for char in counter:
            buckets[counter[char] - 1].append(char)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for char in buckets[i]:
                res.append(char * (i + 1))
        return "".join(res)
