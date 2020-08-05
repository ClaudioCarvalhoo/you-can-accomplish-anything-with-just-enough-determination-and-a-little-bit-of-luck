# O(n)
# n = len(s)

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ['' for _ in s]
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return ''.join(res)