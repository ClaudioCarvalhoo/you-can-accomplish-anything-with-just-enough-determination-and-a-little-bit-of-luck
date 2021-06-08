# O(n*m)
# n = n | m = maxSize(res)


class Solution:
    def countAndSay(self, n: int) -> str:
        res = ["1"]
        for _ in range(1, n):
            res = self.helper(res)
        return "".join(res)

    def helper(self, sequence):
        res = []
        groupChar = sequence[0]
        groupSize = 0
        for i in range(len(sequence)):
            if sequence[i] == groupChar:
                groupSize += 1
            else:
                res += [str(groupSize), groupChar]
                groupChar = sequence[i]
                groupSize = 1
        res += [str(groupSize), groupChar]
        return res