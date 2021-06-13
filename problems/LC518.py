# O(n*m)
# n = len(coins) | m = amount


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for t in range(amount + 1):
                if t >= coin:
                    dp[t] += dp[t - coin]
        return dp[amount]