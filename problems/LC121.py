# O(n)
# n = len(prices)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        boughtFor = prices[0]
        for price in prices:
            best = max(best, price - boughtFor)
            boughtFor = min(boughtFor, price)
        return best
