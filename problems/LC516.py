# O(n²)
# n = len(s)


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestPalindromeSubseqBetween(s, 0, len(s) - 1, {})

    def longestPalindromeSubseqBetween(self, s, start, end, dp):
        if (start, end) in dp:
            return dp[(start, end)]
        if start > end:
            return 0
        if start == end:
            return 1
        elif s[start] == s[end]:
            dp[(start, end)] = (
                self.longestPalindromeSubseqBetween(s, start + 1, end - 1, dp) + 2
            )
        else:
            dp[(start, end)] = max(
                self.longestPalindromeSubseqBetween(s, start, end - 1, dp),
                self.longestPalindromeSubseqBetween(s, start + 1, end, dp),
            )
        return dp[(start, end)]