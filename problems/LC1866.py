# O(n*k)


class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        modulo = 10 ** 9 + 7
        dp = {}
        return self.explore(n, k, dp) % modulo

    def explore(self, n, k, dp):
        if (n, k) in dp:
            return dp[(n, k)]
        if k > n or k <= 0:
            return 0
        if n == k:
            return 1

        res = self.explore(n - 1, k - 1, dp)
        res += (n - 1) * self.explore(n - 1, k, dp)

        dp[(n, k)] = res
        return res
