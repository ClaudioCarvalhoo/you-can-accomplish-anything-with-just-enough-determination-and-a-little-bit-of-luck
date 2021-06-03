# O(log(n))
# n = n


class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n < 0:
            x = 1 / x
            n *= -1
        return self.powFactors(x, n, {})

    def powFactors(self, x, n, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        if n == 1:
            return x
        left, right = n // 2, (n // 2) + (n % 2)
        memo[n] = self.powFactors(x, left, memo) * self.powFactors(x, right, memo)
        return memo[n]