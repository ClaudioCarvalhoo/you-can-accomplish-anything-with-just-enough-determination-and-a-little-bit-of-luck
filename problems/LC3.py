# O(n)
# n = len(s)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        window = set()
        start = 0
        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[start])
                start += 1
            window.add(s[i])
            res = max(res, i - start + 1)
        return res