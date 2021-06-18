# O(n²)
# n = len(s)


class Solution:
    def minInsertions(self, s: str) -> int:
        return len(s) - self.largestPalindromicSubsequence(s, 0, len(s) - 1, {})

    def largestPalindromicSubsequence(self, s, start, end, dp):
        if (start, end) in dp:
            return dp[(start, end)]
        if start > end:
            return 0
        if start == end:
            return 1
        if s[start] == s[end]:
            dp[(start, end)] = (
                self.largestPalindromicSubsequence(s, start + 1, end - 1, dp) + 2
            )
        else:
            dp[(start, end)] = max(
                self.largestPalindromicSubsequence(s, start + 1, end, dp),
                self.largestPalindromicSubsequence(s, start, end - 1, dp),
            )
        return dp[(start, end)]