# O(n)
# n = len(s)


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        nextI = 0
        nextD = len(s)

        res = []
        for char in s:
            if char == "D":
                res.append(nextD)
                nextD -= 1
            if char == "I":
                res.append(nextI)
                nextI += 1
        if s[-1] == "D":
            res.append(nextI)
        else:
            res.append(nextD)
        return res