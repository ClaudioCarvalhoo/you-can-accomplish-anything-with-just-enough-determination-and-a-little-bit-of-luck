# O(n)
# n = len(prices)

import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        smallest = math.inf
        for price in prices:
            smallest = min(smallest, price)
            profit = max(profit, price - smallest)

        return profit
