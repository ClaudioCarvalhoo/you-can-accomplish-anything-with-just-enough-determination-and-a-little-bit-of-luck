# O(n)
# n = len(s)


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccurrence = {}
        for i in range(len(s)):
            lastOccurrence[s[i]] = i

        res = []
        partitionStart = 0
        partitionEnd = 0
        for i in range(len(s)):
            partitionEnd = max(partitionEnd, lastOccurrence[s[i]])
            if partitionEnd == i:
                res.append(partitionEnd - partitionStart + 1)
                partitionStart = i + 1
                partitionEnd = i + 1
        return res