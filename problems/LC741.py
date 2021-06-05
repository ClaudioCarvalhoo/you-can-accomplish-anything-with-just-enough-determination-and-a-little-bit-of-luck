# O(n)
# n = len(prices)


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        boughtAt = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < boughtAt:
                boughtAt = prices[i]
            elif prices[i] - boughtAt - fee > 0:
                profit += prices[i] - boughtAt - fee
                boughtAt = prices[i] - fee
        return profit