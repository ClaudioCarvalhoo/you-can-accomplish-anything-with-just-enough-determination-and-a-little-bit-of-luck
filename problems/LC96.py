# O(n²)
# n = n


class Solution:
    def numTrees(self, n: int) -> int:
        return self.explore(n, {})

    def explore(self, n, dp):
        if n in dp:
            return dp[n]
        if n == 0:
            return 1
        res = 0
        for i in range(n):
            configRes = 1
            configRes *= self.explore(i, dp)
            configRes *= self.explore(n - 1 - i, dp)
            res += configRes
        dp[n] = res
        return res