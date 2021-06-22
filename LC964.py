# O(t)
# t = target


class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        return self.solve(x, target, {})

    def solve(self, x, target, dp):
        if x == target:
            return 0
        if target == 1:
            return 1
        if target in dp:
            return dp[target]

        product = x
        multiplications = 0
        while product < target:
            product *= x
            multiplications += 1

        if product == target:
            return multiplications

        # (x*x*...*x*x) - (solve rest)
        candidate1 = float("inf")
        if product < target * 2:
            candidate1 = multiplications + self.solve(x, product - target, dp) + 1

        # (x*x*...*x*x) + (solve remaining)
        product /= x
        candidate2 = float("inf")
        if x > target:
            candidate2 = self.solve(x, target - 1, dp) + 2
        else:
            candidate2 = self.solve(x, target - product, dp) + multiplications

        res = min(candidate1, candidate2)
        dp[target] = res

        return res